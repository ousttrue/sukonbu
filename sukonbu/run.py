import sys
import pathlib
import json
from typing import NamedTuple, Any, List, Dict


class JsonSchema(NamedTuple):
    title: str
    type: str = 'object'
    description: str = ''
    gltf_detailedDescription: str = ''
    # allOf: List[Any] = None
    properties: Dict[str, 'JsonSchema'] = {}
    items: Any = None
    uniqueItems: Any = None
    minItems: Any = None
    pattern: str = ''
    minimum: Any = None
    #
    dependencies: List[Any] = []
    required: List[Any] = []

    @staticmethod
    def from_dict(root: Dict[str, Any]) -> 'JsonSchema':
        def traverse(node: Dict[str, Any]):
            props = node.get('properties')
            if props:
                for key, prop in props.items():
                    traverse(prop)
                    if 'title' not in prop:
                        prop['title'] = key
                node['properties'] = {
                    key: JsonSchema(**prop)
                    for key, prop in props.items()
                }

        traverse(root)
        return JsonSchema(**root)

    def __str__(self) -> str:
        return f'[{self.title}: {self.type}]'

    def print_tree(self, indent=''):
        print(f'{indent}{self}')
        for key, prop in self.properties.items():
            prop.print_tree(indent + '  ')


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
                    #
                    'additionalProperties',
                    'items',
                    'uniqueItems',
                    'minItems',
                    'pattern',
                    'minimum',
                    #
                    'required',
                    'dependencies',
            ]:
                pass
            elif key == '$ref':
                ref = preprocess(path.parent / node[key])
                node[key] = ref
            else:
                raise Exception(f'unknown {key}')

    traverse(parsed, [])
    return parsed


def process(entry_point: pathlib.Path):
    print(entry_point)
    parsed = preprocess(entry_point)
    root = JsonSchema.from_dict(parsed)
    root.print_tree()


def main():
    path = sys.argv[1]
    process(pathlib.Path(path))


if __name__ == '__main__':
    main()
