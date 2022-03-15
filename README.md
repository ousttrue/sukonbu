# GltfFormat

## gltfformat

generated gltf reader.

## sukonbu

JSON Schema converter.
A code generator for GLTF read/write.

JSON Schema is not compatible with statically typed serialization.
For example, a statically typed language cannot assign `null` to an `int` field.
However, JSON Schema can skip unnecessary object properties, which are manipulated as `null`.

So I made this.

* generate serialized containers(Force all object properties to be nullable)
* generate deserializer for that containers
* generate serializer for that containers(Skip unnecessary object properties)

### ToDo

* [x] python generator(TypedDict)
* [ ] (WIP)D generator
* [ ] C# generator
* [x] (WIP)C++ generator
* [x] manipulate Extensions and Extras

### Usage

```
$ python -m sukonbu.cli PATH_TO_GLTF_JSONSCHEMA --lang python --dst PATH_TO_GENERATE_FILE
```

### examples

#### extension handling

```py
    unlit_path = gltf_path.parent.parent.parent.parent / 'extensions/2.0/Khronos/KHR_materials_unlit/schema/gltf.KHR_materials_unlit.schema.json'
    unlit = JsonSchemaParser(gltf_path.parent)
    unlit.process(unlit_path)
    js_parser.set('materials[].extensions.KHR_materials_unlit', unlit)
```

#### python3 with typing

```py
class MeshPrimitiveRequired(TypedDict):
    # A dictionary object, where each key corresponds to mesh attribute semantic and each value is the index of the accessor containing attribute's data.
    attributes: Dict[str, int]


class MeshPrimitiveOptional(TypedDict, total=False):
    # The index of the accessor that contains the indices.
    indices: int
    # The index of the material to apply to this primitive when rendering.
    material: int
    # The type of primitives to render.
    # default=4
    mode: MeshPrimitiveMode
    # An array of Morph Targets, each  Morph Target is a dictionary mapping attributes (only `POSITION`, `NORMAL`, and `TANGENT` supported) to their deviations in the Morph Target.
    targets: List[Dict[str, int]]
    # Dictionary object with extension-specific objects.
    extensions: dict
    # Application-specific data.
    extras: dict


class MeshPrimitive(MeshPrimitiveRequired, MeshPrimitiveOptional):
    pass
```
