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
        dst = {}
{%- for read in reads %}
        {{ read }}
{%- endfor %}
        return {{ class_name }}(dst)

''')

PYTHON_CLASS = Template('''

class {{ class_name }}(NamedTuple):
{%- for prop in props %}
    # {{ prop[0] }}
    {{ prop[1] }}
{%- endfor %}

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
{%- for write in writes %}
        {{ write }}
{%- endfor %}
        return d

    @staticmethod
    def from_dict(src: dict) -> '{{ class_name }}':
        dst = {}
{%- for read in reads %}
        {{ read }}
{%- endfor %}
        return {{ class_name }}(**dst)

''')


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
        return js.title

    if js.type == 'integer':
        return 'int'
    if js.type == 'number':
        return 'float'
    elif js.type == 'boolean':
        return 'bool'
    elif js.type == 'string':
        return 'str'
    elif js.type == 'array':
        return f'List[{js_to_pythontype(name, js.items, js)}]'
    elif js.type == 'unknown':
        return 'Dict[str, Any]'
    else:  # js.type == 'object' or else
        if js.properties and js.additionalProperties:
            raise Exception()
        if js.properties:
            return js.get_class_name()
        elif js.additionalProperties:
            return f'Dict[str, {js_to_pythontype(name, js.additionalProperties, js)}]'
        else:
            return 'Dict[str, Any]'


def add_optional(src: str, required: bool) -> str:
    if required:
        return f'{src}'

    # if src.startswith('Dict['):
    #     return f'{src}'
    # elif src.startswith('List['):
    #     return f'{src}'
    # else:
    return f'Optional[{src}] = None'


def read_func(name: str, js: JsonSchema, parent: Optional[JsonSchema]) -> str:
    '''
    from_dict
    '''
    if js.get_enum_values():
        return f'if "{name}" in src: dst["{name}"] = {js.title}(src["{name}"]) # noqa'

    if js.properties:
        # object
        return f'if "{name}" in src: dst["{name}"] = {js.get_class_name()}.from_dict(src["{name}"]) # noqa'

    if js.additionalProperties or js.type == 'unknown':
        return f'dst["{name}"] = src.get("{name}", {{}})'

    if js.type == 'array':
        if js.items.properties:
            return f'dst["{name}"] = [{js.items.get_class_name()}.from_dict(item) for item in src["{name}"]] if "{name}" in src else [] # noqa'
        else:
            return f'dst["{name}"] = src.get("{name}", [])'

    # return f'# {name} do nothing'
    return f'if "{name}" in src: dst["{name}"] = src["{name}"] # noqa copy'


def write_func(name: str, js: JsonSchema, parent: Optional[JsonSchema]) -> str:
    '''
    to_dict
    '''
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
    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open('w') as w:

        w.write('''# this is generated by sukonbu
from typing import NamedTuple, List, Any, Optional, Dict
from enum import Enum
''')
        for key, js, parent in schemas:
            enum_values = js.get_enum_values()
            if enum_values:
                if not parent:
                    raise Exception()
                value_map = {
                    'class_name':
                    js.title,
                    'props': [enum_value(value) for value in enum_values],
                    'reads':
                    [read_func(k, v, js) for k, v in js.properties.items()]
                }
                w.write(PYTHON_ENUM.render(**value_map))

            elif js.properties:
                props = [(
                    v.description,
                    f'{k}: {add_optional(js_to_pythontype(k, v, js), k in js.required)}'
                ) for k, v in js.properties.items()]
                value_map = {
                    'class_name':
                    js.get_class_name(),
                    'props':
                    sorted(props, key=lambda x: '=' in x[1]),
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
