import json
import pathlib
from typing import Dict, Optional, NamedTuple, List
from .json_schema import JsonSchema


class JsonSchemaItem(NamedTuple):
    key: str
    item: JsonSchema
    parent: Optional[JsonSchema] = None


class JsonSchemaParser:
    def __init__(self, dir: Optional[pathlib.Path] = None):
        self.root: Optional[JsonSchema] = None
        self.path_map = {}
        self.dir: Optional[pathlib.Path] = dir

    def from_dict(self, root: dict) -> 'JsonSchema':
        '''
        replace dict to JsonSchema by depth first
        '''
        def traverse(node: dict,
                     parent: Optional[dict] = None,
                     key: Optional[str] = None) -> JsonSchema:
            # pass replace leaf to JsonSchema
            props = node.get('properties')
            if props:
                node['properties'] = {
                    key: traverse(prop, node, key)
                    for key, prop in props.items()
                }

            items = node.get('items')
            if items:
                node['items'] = traverse(items, node)

            additionalProperties = node.get('additionalProperties')
            if additionalProperties:
                node['additionalProperties'] = traverse(
                    additionalProperties, node)

            if node.get('anyOf') and parent and key:
                # enum
                node['title'] = parent['title'].replace(
                    ' ', '') + key[0:1].upper() + key[1:]

            if 'properties' not in node: node['properties'] = {}
            if 'dependencies' not in node: node['dependencies'] = []
            if 'required' not in node: node['required'] = []
            return JsonSchema(**node)

        return traverse(root)

    def get_or_read_ref(self, dir: pathlib.Path, filename: str,
                        current: List[str]) -> dict:
        path = dir / filename
        if not path.exists():
            path = self.dir / filename

        # ref = self.path_map.get(path)
        # if ref:
        #     return ref
        text = path.read_text(encoding='utf-8')
        ref_parsed = json.loads(text)
        ref = self.preprocess(ref_parsed, path.parent, current)
        self.path_map[path] = ref
        ref['path'] = path
        return ref

    def preprocess(self, parsed: dict, directory: pathlib.Path,
                   current: List[str]):
        '''
        * `$ref` などを展開して１つの json に連結する
        * allOf を継承と見なして親 JsonSchema の属性を展開する
        * anyOf はひとつめの type と見なす(gltf では enum的に使われる)
        * properties は class として階層化する
        * items は list として階層化する
        * additionalProperties は dict として階層化する
        '''
        if '$schema' in parsed:
            del parsed['$schema']

        if '$ref' in parsed:
            # replace
            # print(path)
            ref = self.get_or_read_ref(directory, parsed['$ref'], current)
            for k, v in ref.items():
                parsed[k] = v
            del parsed['$ref']

        if 'allOf' in parsed:
            # inherited
            ref = self.get_or_read_ref(directory, parsed['allOf'][0]['$ref'],
                                       current)
            for k, v in ref.items():
                if k in parsed:
                    if k == 'properties':
                        for pk, pv in ref[k].items():
                            parsed[k][pk] = pv
                        continue
                    elif k in ['title']:
                        continue
                parsed[k] = v
            del parsed['allOf']

        if 'anyOf' in parsed:
            for x in parsed['anyOf']:
                if 'type' in x:
                    parsed['type'] = x['type']
                    break

        for key in ['not']:
            # skip
            if key in parsed:
                del parsed[key]

        keys = [key for key in parsed.keys()]
        for key in keys:
            if key == 'properties':
                for k, v in parsed[key].items():
                    self.preprocess(v, directory, current + [k])
            elif key == 'items':
                parsed[key] = self.preprocess(parsed[key], directory,
                                              current + ['Item'])  # array item
            elif key == 'additionalProperties':
                tmp = parsed[key]
                if tmp is False:
                    # do nothing
                    continue
                parsed[key] = self.preprocess(tmp, directory,
                                              current + ['Value'])  # kv value
            elif key in [
                    'path',
                    'title',
                    'type',
                    'description',
                    'gltf_detailedDescription',
                    'gltf_webgl',
                    'gltf_uriType',
                    'default',
                    #
                    'enum',
                    #
                    'additionalProperties',
                    'minProperties',
                    #
                    'uniqueItems',
                    'minItems',
                    'maxItems',
                    #
                    'minimum',
                    'maximum',
                    'multipleOf',
                    'exclusiveMinimum',
                    'pattern',
                    'format',
                    #
                    'anyOf',
                    'oneOf',
                    #
                    'required',
                    'dependencies',
            ]:
                pass
            else:
                raise Exception(f'unknown {key}')

        if 'title' not in parsed:
            parsed['title'] = '.'.join(current)
        if parsed['title'] == 'Extension':
            # set name to extension
            if current:
                parsed['title'] = '.'.join(current[0:-1] + [parsed['title']])
        elif parsed['title'] == 'Extras':
            # set name to extras
            if current:
                parsed['title'] = '.'.join(current[0:-1] + [parsed['title']])

        return parsed

    def process(self, entry_point: pathlib.Path):
        text = entry_point.read_text()
        parsed = json.loads(text)
        processed = self.preprocess(parsed, entry_point.parent, [])
        self.root = self.from_dict(processed)
