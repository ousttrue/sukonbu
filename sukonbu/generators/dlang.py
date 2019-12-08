import pathlib
from typing import List, Tuple, Optional
from jinja2 import Template
from ..json_schema import JsonSchema
from ..json_schema_parser import JsonSchemaParser

DLANG_ENUM = Template('''
enum {{ class_name }}
{
{%- for prop in props %}
    {{ prop }},
{%- endfor %}
}

''')

DLANG_CLASS = Template('''
class {{ class_name }}
{
{%- for prop in props %}
    // {{ prop[0] }}
    {{ prop[1] }};
{%- endfor %}

    static {{ class_name }} fromJSON(JSONValue src)
    {
        auto value = new {{ class_name }}();
{%- for read in reads %}
        {{ read }}
{%- endfor %}
        return value;
    }
}

''')


def js_to_dlang_type(name: str, js: JsonSchema, parent: JsonSchema) -> str:
    '''
    convert JsonSchema to dlang type
    '''
    if js.title in ['Extension', 'Extras']:
        return js.get_class_name()

    enum_values = js.get_enum_values()
    if enum_values:
        return get_enum_name(name, js, parent)

    if js.type == 'integer':
        return 'int'
    if js.type == 'number':
        return 'float'
    elif js.type == 'boolean':
        return 'bool'
    elif js.type == 'string':
        return 'string'
    elif js.type == 'object':
        if js.properties and js.additionalProperties:
            raise Exception()
        if js.properties:
            return js.get_class_name()
        elif js.additionalProperties:
            return f'{js_to_dlang_type(name, js.additionalProperties, js)}[string]'
        else:
            return 'Object[string]'
    elif js.type == 'array':
        return f'{js_to_dlang_type(name, js.items, js)}[]'
    elif js.type == 'unknown':
        return 'Object[string]'
    else:
        raise Exception()
        # return js.type, 'None'


def get_enum_name(name: str, js: JsonSchema, parent: JsonSchema) -> str:
    return parent.get_class_name() + name[0:1].upper() + name[1:]


def escape_enum(src: str) -> str:
    splitted = src.split('/')
    if len(splitted) > 1:
        # ex. image/jpg
        return ''.join(x for x in splitted)
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


def add_optional(src: str, required: bool) -> str:
    if src in ['int', 'bool', 'float']:
        return f'Nullable!{src}'
    return f'{src}'


def read_func(name: str, js: JsonSchema, parent: Optional[JsonSchema]) -> str:
    '''
    from_dict
    '''
    return ''


def write_func(name: str, js: JsonSchema, parent: Optional[JsonSchema]) -> str:
    '''
    to_dict
    '''
    return ''


def escape_symbol(name: str) -> str:
    if name in ['version']:
        return name + '_'
    else:
        return name


def read_func(name: str, js: JsonSchema, parent: Optional[JsonSchema]) -> str:
    '''
    fromJSON
    '''
    if js.get_enum_values():
        if not parent:
            raise Exception()
        if js.type == 'string':
            return f'if(const(JSONValue)* x = "{name}" in src){{ value.{escape_symbol(name)} = to!{get_enum_name(name, js, parent)}(x.str); }}'
        else:
            return f'if(const(JSONValue)* x = "{name}" in src){{ value.{escape_symbol(name)} = cast({get_enum_name(name, js, parent)})x.integer; }}'

    if js.properties:
        # object
        return f'if(const(JSONValue)* x = "{name}" in src){{ value.{escape_symbol(name)} = {js.get_class_name()}.fromJSON(src["{name}"]); }}'

    if js.type == 'array':
        items = js.items
        if items.properties:
            return f'if(const(JSONValue)* x = "{name}" in src){{ value.{escape_symbol(name)} = x.array.map!(a => {items.get_class_name()}.fromJSON(a)).array; }}'
        else:
            if items.type == 'integer':
                # must range to array
                # https://stackoverflow.com/questions/13125446/converting-string-to-char?rq=1
                return f'if(const(JSONValue)* x = "{name}" in src){{ value.{escape_symbol(name)} = x.array.map!(a => cast(int)a.integer).array; }}'
            elif items.type == 'number':
                return f'if(const(JSONValue)* x = "{name}" in src){{ value.{escape_symbol(name)} = x.array.map!(a => a.asFloat).array; }}'
            elif items.type == 'string':
                return f'if(const(JSONValue)* x = "{name}" in src){{ value.{escape_symbol(name)} = x.array.map!(a => a.str).array; }}'
            elif items.additionalProperties:
                if items.additionalProperties.type == 'integer':
                    return f'if(const(JSONValue)* x = "{name}" in src){{ value.{escape_symbol(name)} = x.array.map!(a => a.object.byPair.map!(kv => tuple(kv.key, cast(int)kv.value.integer)).assocArray).array; }}'

                else:
                    raise NotImplementedError()

    if js.type == 'integer':
        return f'if(const(JSONValue)* x = "{name}" in src){{ value.{escape_symbol(name)} = nullable(cast(int)x.integer); }}'
    elif js.type == 'number':
        return f'if(const(JSONValue)* x = "{name}" in src){{ value.{escape_symbol(name)} = nullable(x.asFloat); }}'
    elif js.type == 'string':
        return f'if(const(JSONValue)* x = "{name}" in src){{ value.{escape_symbol(name)} = x.str; }}'
    elif js.type == 'boolean':
        return f'if(const(JSONValue)* x = "{name}" in src){{ value.{escape_symbol(name)} = x.boolean; }}'

    return f'// not implemented: {js.type}'


def generate(parser: JsonSchemaParser, dst: pathlib.Path) -> None:
    if not parser.root:
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

    traverse('', parser.root, None)

    print(f'write: {dst}')
    with dst.open('w') as w:
        w.write('''// this is generated by sukonbu
import std.typecons;
import std.json;
import std.conv;
import std.algorithm;
import std.array;


float asFloat(const JSONValue value)
{
    return asFloat(&value); 
}
float asFloat(const JSONValue* value)
{
    if(value.type == JSONType.float_)
    {
        return cast(float)value.floating;
    }
    else if(value.type== JSONType.integer)
    {
        return cast(float)value.integer;
    }
    else{
        throw new Exception("type error");
    }
}

''')

        for key, js, parent in schemas:
            enum_values = js.get_enum_values()
            if enum_values:
                if not parent:
                    raise Exception()
                value_map = {
                    'class_name': get_enum_name(key, js, parent),
                    'props': [enum_value(value) for value in enum_values],
                }
                w.write(DLANG_ENUM.render(**value_map))

            elif js.title in ['Extension', 'Extras']:
                if not parent:
                    raise Exception()
                value_map = {
                    'class_name': js.get_class_name(),
                    'props': [],
                    'writes': [],
                    'reads': [],
                }
                w.write(DLANG_CLASS.render(**value_map))

            elif js.properties:
                props = [(
                    v.description,
                    f'{add_optional(js_to_dlang_type(k, v, js), k in js.required)} {escape_symbol(k)}'
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
                w.write(DLANG_CLASS.render(**value_map))
