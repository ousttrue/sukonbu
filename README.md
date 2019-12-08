# sukonbu

JSON Schema converter.
A code generator for GLTF read/write.

JSON Schema is not compatible with statically typed serialization.
For example, a statically typed language cannot assign `null` to an `int` field.
However, JSON Schema can skip unnecessary object properties, which are manipulated as `null`.

So I made this.

* generate serialized containers(Force all object properties to be nullable)
* generate deserializer for that containers
* generate serializer for that containers(Skip unnecessary object properties)

## ToDo

* [x] python generator
* [WIP] D generator
* [ ] C# generator
* [ ] C++ generator
* [ ] manipulate Extensions and Extras

## Usage

```
$ python -m sukonbu.cli PATH_TO_GLTF_JSONSCHEMA --lang python --dst PATH_TO_GENERATE_FILE
```

## examples

### python3 with typing

```py
class MeshPrimitive(NamedTuple):
    # A dictionary object, where each key corresponds to mesh attribute semantic and each value is the index of the accessor containing attribute's data.
    attributes: Optional[Dict[str, int]] = None
    # The index of the bufferView.
    indices: Optional[int] = None
    # The index of the bufferView.
    material: Optional[int] = None
    # The type of primitives to render.
    mode: Optional[MeshPrimitiveMode] = None
    # An array of Morph Targets, each  Morph Target is a dictionary mapping attributes (only `POSITION`, `NORMAL`, and `TANGENT` supported) to their deviations in the Morph Target.
    targets: Optional[List[Dict[str, int]]] = None
    # Dictionary object with extension-specific objects.
    extensions: Optional[Dict[str, Any]] = None
    # Application-specific data.
    extras: Optional[Dict[str, Any]] = None
```
