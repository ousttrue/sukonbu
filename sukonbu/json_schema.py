from typing import NamedTuple, Any, Optional, List, Dict
import pathlib


class JsonSchema(NamedTuple):
    path: Optional[pathlib.Path] = None
    title: str = ''
    type: str = 'unknown'
    description: str = ''
    gltf_detailedDescription: str = ''
    default: Any = None
    gltf_webgl: Any = None
    gltf_uriType: Any = None
    properties: Dict[str, Any] = {}
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
    dependencies: List[Any] = []
    required: List[Any] = []

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
        name = ''
        if self.path:
            name = f': {self.path.name}'
        if self.title:
            return f'[{self.title}: {self.type}{name}]'
        else:
            pass
            a = 0
