from typing import NamedTuple, Any, Optional, List, Dict
import pathlib
import re

JS_PATH_EXTRACT = re.compile(r'^(\w+)(.*)')


class JsonSchema(NamedTuple):
    path: Optional[pathlib.Path] = None
    title: str = ''
    type: str = 'unknown'
    description: str = ''
    gltf_detailedDescription: str = ''
    default: Any = None
    gltf_webgl: Any = None
    gltf_uriType: Any = None
    properties: Dict[str, Any] = None
    oneOf: Any = None
    anyOf: Any = None
    enum: Any = None
    #
    additionalProperties: Any = None
    minProperties: Any = None
    items: Any = None
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
    dependencies: List[Any] = None
    required: List[Any] = None

    def get_enum_values(self) -> List[Any]:
        if self.anyOf:

            def enum_value(value):
                if self.type in 'string':
                    return value['enum'][0]
                else:
                    return f'{value["description"]}={value["enum"][0]}'

            return [
                enum_value(value) for value in self.anyOf if 'enum' in value
            ]

        return []

    def title_or_type(self):
        value = f'{self.title}({self.type})' if self.title else self.type

        enum_values = self.get_enum_values()
        if enum_values:
            value = f'enum {value} {{' + ', '.join(enum_values) + '}'
        # if self.path:
        #     value += ': ' + self.path.name
        return value

    def __str__(self):
        if self.type == 'object':
            return self.title_or_type()
        elif self.type == 'array':
            return f'{self.items.title_or_type()}[]'
        else:
            return self.title_or_type()

    def get_class_name(self):
        if self.type in [
                'null', 'bool', 'int', 'number', 'string', 'object', 'array', 'unknown',
        ]:
            if self.properties:
                title = self.title
                if '.' in self.title:
                    splited = self.title.split('.')
                    title = ''.join(s[0].upper() + s[1:] for s in splited)
                return title.replace(' ', '')

        return self.type

    def set(self, json_path: str, schema):
        print(json_path)
        m = JS_PATH_EXTRACT.match(json_path)
        head = m[1]
        if not m[2]:
            self.properties[head] = schema
            return

        # recursive
        tail = m[2]
        child = self.properties[head]
        if m[2].startswith('.'):
            tail = m[2][1:]
            child.set(tail, schema)
        elif tail.startswith('[]'):
            tail = m[2][3:]
            child.items.set(tail, schema)
        else:
            raise NotImplementedError()
