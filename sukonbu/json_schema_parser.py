import json
import pathlib
from typing import Dict, Optional, List, Tuple
from jinja2 import Template
from .json_schema import JsonSchema

PYTHON_TEMPLATE = Template('''

class {{ class_name }}(NamedTuple):
{%- for prop in props %}
    # {{ prop[0] }}
    {{ prop[1] }}
{%- endfor %}

    @staticmethod
    def from_json(src: dict) -> '{{ class_name }}':
{%- for init in inits %}
        {{ init }}
{%- endfor %}
        return {{ class_name }}(**src)

''')


class JsonSchemaParser:
    def __init__(self):
        self.root: Optional[JsonSchema] = None
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
                    'anyOf',
                    'oneOf',
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
        self.root = self.from_dict(processed)

    def print(self) -> None:
        for key, js in self.schema_map.items():
            print(js)
            print('{')
            for k, v in js.properties.items():
                print(f'  {k}: {v}')
            print('}')

    def generate(self, dst: pathlib.Path) -> None:
        if not self.root:
            return

        schemas: List[JsonSchema] = []

        def traverse(js: JsonSchema):
            for k, v in js.properties.items():
                traverse(v)
            if js.items:
                traverse(js.items)
            if js not in schemas:
                schemas.append(js)

        traverse(self.root)

        def js_to_pythontype(js: JsonSchema) -> Tuple[str, str]:
            if js.title == 'Extension':
                return 'dict', '{}'

            if js.type == 'integer':
                return 'int', '0'
            if js.type == 'number':
                return 'float', '0.0'
            elif js.type == 'boolean':
                return 'bool', 'False'
            elif js.type == 'string':
                return 'str', "''"
            elif js.type == 'object':
                if js.properties:
                    name = js.get_class_name()
                    return name, f'{name}()'
                return 'Any', 'None'
            elif js.type == 'array':
                return f'List[{js_to_pythontype(js.items)[0]}]', '[]'
            elif js.type == 'unknown':
                return 'Any', 'None'
            else:
                return js.type, 'None'

        def type_with_default(src: Tuple[str, str]) -> str:
            return f'{src[0]} = {src[1]}'

        def init_func(name: str, js: JsonSchema) -> str:
            if js.properties:
                return f'if "{name}" in src: src["{name}"] = {js.get_class_name()}.from_json(src["{name}"]) # noqa'

            if js.type == 'array' and js.items.properties:
                return f'if "{name}" in src: src["{name}"] = [{js.items.get_class_name()}.from_json(item) for item in src["{name}"]] # noqa'

            return f'# {name} do nothing'
            # return f'src["{name}]'

        print(f'write: {dst}')
        with dst.open('w') as w:

            w.write('''from typing import NamedTuple, List, Any
''')
            for js in schemas:
                if js.properties:
                    value_map = {
                        'class_name':
                        js.get_class_name(),
                        'props':
                        [(v.description,
                          f'{k}: {type_with_default(js_to_pythontype(v))}')
                         for k, v in js.properties.items()],
                        'inits':
                        [init_func(k, v) for k, v in js.properties.items()]
                    }
                    w.write(PYTHON_TEMPLATE.render(**value_map))

            w.write('''

if __name__ == '__main__':
    gltf = glTF()
    print(gltf)
''')
