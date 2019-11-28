import sys
import pathlib
import json
import io
from typing import NamedTuple, Any, List, Dict, Optional, TextIO


class JsonSchema(NamedTuple):
    title: str = ''
    type: str = 'object'
    description: str = ''
    gltf_detailedDescription: str = ''
    default: Any = None
    gltf_webgl: Any = None
    gltf_uriType: Any = None
    properties: Dict[str, 'JsonSchema'] = {}
    #
    additionalProperties: Any = None
    minProperties: Any = None
    items: Optional['JsonSchema'] = None
    uniqueItems: Any = None
    minItems: Any = None
    maxItems: Any = None
    pattern: str = ''
    format: str = ''
    minimum: Any = None
    maximum: Any = None
    exclusiveMinimum: Any = None
    multipleOf: Any = None
    #
    dependencies: List[Any] = []
    required: List[Any] = []

    @staticmethod
    def from_dict(root: Dict[str, Any]) -> 'JsonSchema':
        def traverse(node: Dict[str, Any]):
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
            return JsonSchema(**node)

        return traverse(root)

    def traverse(self):
        if self.type == 'array':
            for x in self.items.traverse():
                yield x
        elif self.type == 'object':
            for k, v in self.properties.items():
                for x in v.traverse():
                    yield x
        yield self

    def __str__(self):
        return f'[{self.title}: {self.type}]'


def preprocess(path: pathlib.Path):
    text = path.read_text()
    parsed = json.loads(text)
    if not isinstance(parsed, dict):
        raise TypeError('not dict')

    def traverse(node, parents):
        keys = [key for key in node.keys()]
        for key in keys:
            if key == '$schema':
                del node['$schema']
            # elif key == '$ref':
            #     ref = dir / node[key]
            #     print(ref)
            #     raise NotImplementedError()
            elif key == 'properties':
                for k, v in node[key].items():
                    traverse(v, parents + [k])
            elif key == 'items':
                items = traverse(node[key], parents + ['[]'])
                node[key] = items
            elif key == 'allOf':
                value = node[key]
                if len(value) == 1:
                    # inherit $ref
                    ref = preprocess(path.parent / value[0]['$ref'])
                    for k, v in ref.items():
                        # add members
                        if k in node:
                            NotImplementedError()
                        else:
                            node[k] = v
                    del node[key]
                else:
                    raise NotImplementedError()
            elif key in [
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
            elif key in ['anyOf', 'not', 'oneOf']:
                del node[key]
            elif key == '$ref':
                ref = preprocess(path.parent / node[key])
                node = ref
            else:
                raise Exception(f'unknown {key}')
        return node

    return traverse(parsed, [])


def process(entry_point: pathlib.Path):
    print(entry_point)
    parsed = preprocess(entry_point)
    root = JsonSchema.from_dict(parsed)
    # sio = io.StringIO()
    # print(sio.getvalue())

    for js in root.traverse():
        if js.type == 'object':
            print(js)


def main():
    path = sys.argv[1]
    process(pathlib.Path(path))


if __name__ == '__main__':
    main()
