from typing import NamedTuple, Any, Optional, List, Dict
import pathlib
import re

JS_PATH_EXTRACT = re.compile(r'^(\w+)(.*)')


class JsonSchema:

    def __init__(self, **kw):
        self.path: Optional[pathlib.Path] = kw.get('path')
        self.title: str = kw.get('title', '')
        self.type: str = kw.get('type', 'unknown')
        self.description: str = kw.get('description', '')
        self.gltf_detailedDescription: str = kw.get('gltf_detailedDescription', '')
        self.default: Any = kw.get('default')
        self.gltf_webgl: Any = kw.get('gltf_webgl')
        self.gltf_uriType: Any = kw.get('gltf_uriType')
        self.properties: Dict[str, Any] = kw.get('properties', {})
        self.oneOf: Any = kw.get('oneOf')
        self.anyOf: Any = kw.get('anyOf')
        self.enum: Any = kw.get('enum')
        #
        self.additionalProperties: Any = kw.get('additionalProperties')
        self.minProperties: Any = kw.get('minProperties')
        self.items: Any = kw.get('items')
        self.uniqueItems: Any = kw.get('uniqueItems')
        self.minItems: Any = kw.get('minItems')
        self.maxItems: Any = kw.get('maxItems')
        self.pattern: str = kw.get('pattern', '')
        self.format: str = kw.get('format', '')
        self.minimum: Any = kw.get('minimum')
        self.maximum: Any = kw.get('maximum')
        self.exclusiveMinimum: Any = kw.get('exclusiveMinimum')
        self.multipleOf: Any = kw.get('multipleOf')
        #
        self.dependencies: List[Any] = kw.get('dependencies', [])
        self.required: List[Any] = kw.get('required', [])

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
                'null',
                'bool',
                'int',
                'number',
                'string',
                'object',
                'array',
                'unknown',
        ]:
            if self.properties:
                title = self.title
                if '.' in self.title:
                    splited = self.title.split('.')
                    title = ''.join(s[0].upper() + s[1:] for s in splited)
                return title.replace(' ', '')

        return self.type

    def set(self, json_path: str, schema):
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
