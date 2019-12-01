# sukonbu

JSON Schema converter.
A code generator for GLTF read/write.

JSON Schema is not compatible with statically typed serialization.
For example, a statically typed language cannot assign `null` to an `int` field.
However, JSON Schema can skip unnecessary object properties, which are manipulated as `null`.

So I made this.

* generate serialized containers(Force all fields to be nullable)
* generate deserializer for that containers
* generate serializer(Skip unnecessary object properties) for that containers.

## ToDo

* [ ] WIP python generator
* [ ] C# generator
* [ ] D generator
* [ ] C++ generator

## Usage

TODO:
