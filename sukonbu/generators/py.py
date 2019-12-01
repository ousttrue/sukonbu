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

    def to_dict(self):
        return self.value

    @staticmethod
    def from_dict(src) -> '{{ class_name }}':
{%- for read in reads %}
        {{ read }}
{%- endfor %}
        return {{ class_name }}(src)

''')

PYTHON_CLASS = Template('''

class {{ class_name }}(NamedTuple):
{%- for prop in props %}
    # {{ prop[0] }}
    {{ prop[1] }}
{%- endfor %}

    def to_dict(self) -> dict:
        d = {}
{%- for write in writes %}
        {{ write }}
{%- endfor %}
        return d

    @staticmethod
    def from_dict(src: dict) -> '{{ class_name }}':
{%- for read in reads %}
        {{ read }}
{%- endfor %}
        return {{ class_name }}(**src)

''')


def get_class_name(name: str, js: JsonSchema,
                   parent: Optional[JsonSchema]) -> str:
    if parent and js.get_enum_values():
        # enum
        return parent.get_class_name() + name[0:1].upper() + name[1:]
    else:
        return js.get_class_name()


def js_to_pythontype(name: str, js: JsonSchema, parent: JsonSchema) -> str:
    '''
    convert JsonSchema to pythontype

    * Extension: ToDo
    * Extra: ToDo

    * object with additionalProperties => Dict[str, T]
    * array => List[T]
    * else => Optional[T]
    '''
    if js.title == 'Extension':
        return 'Dict[str, Any]'

    enum_values = js.get_enum_values()
    if enum_values:
        return get_class_name(name, js, parent)

    if js.type == 'integer':
        return 'int'
    if js.type == 'number':
        return 'float'
    elif js.type == 'boolean':
        return 'bool'
    elif js.type == 'string':
        return 'str'
    elif js.type == 'object':
        if js.properties and js.additionalProperties:
            raise Exception()
        if js.properties:
            return js.get_class_name()
        elif js.additionalProperties:
            return f'Dict[str, {js_to_pythontype(name, js.additionalProperties, js)}]'
        else:
            return 'Dict[str, Any]'
    elif js.type == 'array':
        return f'List[{js_to_pythontype(name, js.items, js)}]'
    elif js.type == 'unknown':
        return 'Dict[str, Any]'
    else:
        raise Exception()
        # return js.type, 'None'


def type_with_default(src: str) -> str:
    # if src.startswith('Dict['):
    #     return f'{src} = {{}}'
    # elif src.startswith('List['):
    #     return f'{src} = []'
    # else:
    return f'Optional[{src}] = None'


def read_func(name: str, js: JsonSchema, parent: Optional[JsonSchema]) -> str:
    '''
    replace Enum and Object values
    '''
    if js.get_enum_values():
        return f'if "{name}" in src: src["{name}"] = {get_class_name(name, js, parent)}(src["{name}"]) # noqa'

    if js.properties:
        # object
        return f'if "{name}" in src: src["{name}"] = {js.get_class_name()}.from_dict(src["{name}"]) # noqa'

    if js.type == 'array' and js.items.properties:
        return f'if "{name}" in src: src["{name}"] = [{js.items.get_class_name()}.from_dict(item) for item in src["{name}"]] # noqa'

    return f'# {name} do nothing'


def write_func(name: str, js: JsonSchema, parent: Optional[JsonSchema]) -> str:
    condition = f'if self.{name} is not None: '

    if js.properties or js.get_enum_values():
        return f'{condition}d["{name}"] = self.{name}.to_dict() # noqa'

    if js.type == 'array':
        condition = f'if self.{name}: '
        if js.items.properties:
            return f'{condition}d["{name}"] = [item.to_dict() for item in self.{name}] # noqa'

    return f'{condition}d["{name}"] = self.{name} # noqa'


def escape_enum(src: str) -> str:
    splitted = src.split('/')
    if len(splitted) > 1:
        # ex. image/jpg
        return ''.join(x.title() for x in splitted)
    else:
        return src


def enum_value(src: str) -> str:
    splitted = src.split('=')
    if len(splitted) == 2:
        # int
        return f'{escape_enum(splitted[0])} = {splitted[1]}'
    else:
        # str
        return f'{escape_enum(splitted[0])} = "{splitted[0]}"'


def generate(self: JsonSchemaParser, dst: pathlib.Path) -> None:
    if not self.root:
        return

    used: List[JsonSchema] = []
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

    print(f'write: {dst}')
    with dst.open('w') as w:

        w.write('''# this is generated by sukonbu
from typing import NamedTuple, List, Any, Optional, Dict
from enum import Enum
''')
        for key, js, parent in schemas:
            enum_values = js.get_enum_values()
            if enum_values:
                value_map = {
                    'class_name':
                    get_class_name(key, js, parent),
                    'props': [enum_value(value) for value in enum_values],
                    'reads':
                    [read_func(k, v, js) for k, v in js.properties.items()]
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
                    'writes':
                    [write_func(k, v, js) for k, v in js.properties.items()],
                    'reads':
                    [read_func(k, v, js) for k, v in js.properties.items()]
                }
                w.write(PYTHON_CLASS.render(**value_map))

        w.write('''

if __name__ == '__main__':
    gltf = glTF()
    print(gltf)
''')
