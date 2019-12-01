import pathlib
from typing import List, Tuple, Optional
from jinja2 import Template
from ..json_schema import JsonSchema
from ..json_schema_parser import JsonSchemaParser

PYTHON_ENUM = Template('''

class {{ class_name }}(Enum):
{%- for prop in props %}
    {{ prop }}
{%- endfor %}

    @staticmethod
    def from_json(src) -> '{{ class_name }}':
{%- for init in inits %}
        {{ init }}
{%- endfor %}
        return {{ class_name }}(src)

''')

PYTHON_CLASS = Template('''

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

    used = []
    schemas: List[Tuple[str, JsonSchema, Optional[JsonSchema]]] = []

    def traverse(name: str, js: JsonSchema, parent: Optional[JsonSchema]):
        for k, v in js.properties.items():
            traverse(k, v, js)
        if js.items:
            traverse('[]', js.items, js)
        if js not in used:
            schemas.append((name, js, parent))
            used.append(js)

    traverse('', self.root, None)

    def get_class_name(name: str, js: JsonSchema,
                       parent: Optional[JsonSchema]) -> str:
        if parent and js.get_enum_values():
            return parent.get_class_name() + name[0:1].upper() + name[1:]
        else:
            return js.get_class_name()

    def js_to_pythontype(name: str, js: JsonSchema,
                         parent: JsonSchema) -> Tuple[str, str]:
        if js.title == 'Extension':
            return 'dict', '{}'

        enum_values = js.get_enum_values()
        if enum_values:
            default = js.default
            cls_name = get_class_name(name, js, parent)
            if js.type == 'string' and default:
                default = f'"{default}"'
            if default:
                default = f'{cls_name}({default})'
            return cls_name, default

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
            return f'List[{js_to_pythontype(name, js.items, js)[0]}]', '[]'
        elif js.type == 'unknown':
            return 'Any', 'None'
        else:
            return js.type, 'None'

    def type_with_default(src: Tuple[str, str]) -> str:
        return f'{src[0]} = {src[1]}'

    def init_func(name: str, js: JsonSchema, parent: Optional[JsonSchema]) -> str:
        if js.get_enum_values():
            return f'if "{name}" in src: src["{name}"] = {get_class_name(name, js, parent)}(src["{name}"]) # noqa'

        if js.properties:
            return f'if "{name}" in src: src["{name}"] = {js.get_class_name()}.from_json(src["{name}"]) # noqa'

        if js.type == 'array' and js.items.properties:
            return f'if "{name}" in src: src["{name}"] = [{js.items.get_class_name()}.from_json(item) for item in src["{name}"]] # noqa'

        return f'# {name} do nothing'
        # return f'src["{name}]'

    def escape_enum(src: str) -> str:
        splitted = src.split('/')
        if len(splitted) > 1:
            return ''.join(x.title() for x in splitted)
        else:
            return src

    def enum_value(src: str) -> str:
        splitted = src.split('=')
        if len(splitted) == 2:
            return f'{escape_enum(splitted[0])} = {splitted[1]}'
        else:
            return f'{escape_enum(splitted[0])} = "{splitted[0]}"'

    print(f'write: {dst}')
    with dst.open('w') as w:

        w.write('''from typing import NamedTuple, List, Any
from enum import Enum
''')
        for key, js, parent in schemas:
            enum_values = js.get_enum_values()
            if enum_values:
                value_map = {
                    'class_name': get_class_name(key, js, parent),
                    'props': [enum_value(value) for value in enum_values],
                    'inits':
                    [init_func(k, v, js) for k, v in js.properties.items()]
                }
                w.write(PYTHON_ENUM.render(**value_map))

            elif js.properties:
                value_map = {
                    'class_name':
                    js.get_class_name(),
                    'props':
                    [(v.description,
                      f'{k}: {type_with_default(js_to_pythontype(k, v, js))}')
                     for k, v in js.properties.items()],
                    'inits':
                    [init_func(k, v, js) for k, v in js.properties.items()]
                }
                w.write(PYTHON_CLASS.render(**value_map))

        w.write('''

if __name__ == '__main__':
    gltf = glTF()
    print(gltf)
''')
