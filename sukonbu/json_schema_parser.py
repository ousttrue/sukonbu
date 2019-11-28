import json
import pathlib
from typing import Dict
from .json_schema import JsonSchema


class JsonSchemaParser:
    def __init__(self):
        self.path_map = {}
        self.schema_map: Dict[str, JsonSchema] = {}

    def from_dict(self, root: dict) -> 'JsonSchema':
        '''
        replace dict to JsonSchema by depth first
        '''
        def traverse(node: dict):
            # pass replace leaf to JsonSchema
            props = node.get('properties')
            if props:
                node['properties'] = {
                    key: traverse(prop)
                    for key, prop in props.items()
                }
            items = node.get('items')
            if items:
                node['items'] = traverse(items)

            path = node.get('path')
            if path:
                if path in self.schema_map:
                    return self.schema_map[path]

            js = JsonSchema(**node)
            if path:
                self.schema_map[path] = js
            return js

        return traverse(root)

    def get_or_read_ref(self, path: pathlib.Path) -> dict:
        ref = self.path_map.get(path)
        if ref:
            return ref
        text = path.read_text()
        ref_parsed = json.loads(text)
        ref = self.preprocess(ref_parsed, path.parent)
        self.path_map[path] = ref
        ref['path'] = path
        return ref

    def preprocess(self, parsed: dict, directory: pathlib.Path):
        if '$schema' in parsed:
            del parsed['$schema']

        if '$ref' in parsed:
            # replace
            path = directory / parsed['$ref']
            # print(path)
            ref = self.get_or_read_ref(path)
            for k, v in ref.items():
                parsed[k] = v
            del parsed['$ref']

        if 'allOf' in parsed:
            # inherited
            path = directory / parsed['allOf'][0]['$ref']
            ref = self.get_or_read_ref(path)
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

        for key in ['anyOf', 'not', 'oneOf']:
            # skip
            if key in parsed:
                del parsed[key]

        keys = [key for key in parsed.keys()]
        for key in keys:
            if key == 'properties':
                for k, v in parsed[key].items():
                    self.preprocess(v, directory)
            elif key == 'items':
                parsed[key] = self.preprocess(parsed[key], directory)
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
                    #
                    'required',
                    'dependencies',
            ]:
                pass
            else:
                raise Exception(f'unknown {key}')

        return parsed

    def process(self, entry_point: pathlib.Path):
        print(entry_point)
        text = entry_point.read_text()
        parsed = json.loads(text)
        processed = self.preprocess(parsed, entry_point.parent)
        root = self.from_dict(processed)
