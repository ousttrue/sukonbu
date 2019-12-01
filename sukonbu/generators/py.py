import pathlib
from typing import List, Tuple
from jinja2 import Template
from ..json_schema import JsonSchema
from ..json_schema_parser import JsonSchemaParser

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


def generate(self: JsonSchemaParser, dst: pathlib.Path) -> None:
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
