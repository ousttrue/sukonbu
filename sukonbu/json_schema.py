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

    def title_of_type(self):
        return self.title if self.title else self.type

    def __str__(self):
        if self.type == 'object':
            return self.title_of_type()
        elif self.type == 'array':
            return f'{self.items.title_of_type()}[]'
        else:
            return self.type
