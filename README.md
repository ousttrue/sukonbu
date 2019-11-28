# sukonbu

JSON Schema converter.
A code generator for GLTF read/write.

## ToDo

* [ ] python generator
* [ ] C# generator
* [ ] D generator
* [ ] C++ generator

## log

parse https://github.com/KhronosGroup/glTF/blob/master/specification/2.0/schema/glTF.schema.json

```
glTF Id(integer)
{
}
Extension(object)
{
}
Extras(unknown)
{
}
Accessor Sparse Indices(object)
{
  bufferView: glTF Id(integer)
  byteOffset: integer
  componentType: enum integer {UNSIGNED_BYTE=5121, UNSIGNED_SHORT=5123, UNSIGNED_INT=5125}
  extensions: Extension(object)
  extras: Extras(unknown)
}
Accessor Sparse Values(object)
{
  bufferView: glTF Id(integer)
  byteOffset: integer
  extensions: Extension(object)
  extras: Extras(unknown)
}
Accessor Sparse(object)
{
  count: integer
  indices: Accessor Sparse Indices(object)
  values: Accessor Sparse Values(object)
  extensions: Extension(object)
  extras: Extras(unknown)
}
Accessor(object)
{
  bufferView: glTF Id(integer)
  byteOffset: integer
  componentType: enum integer {BYTE=5120, UNSIGNED_BYTE=5121, SHORT=5122, UNSIGNED_SHORT=5123, UNSIGNED_INT=5125, FLOAT=5126}
  normalized: boolean
  count: integer
  type: enum string {SCALAR, VEC2, VEC3, VEC4, MAT2, MAT3, MAT4}
  max: number[]
  min: number[]
  sparse: Accessor Sparse(object)
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
Animation Channel Target(object)
{
  node: glTF Id(integer)
  path: enum string {translation, rotation, scale, weights}
  extensions: Extension(object)
  extras: Extras(unknown)
}
Animation Channel(object)
{
  sampler: glTF Id(integer)
  target: Animation Channel Target(object)
  extensions: Extension(object)
  extras: Extras(unknown)
}
Animation Sampler(object)
{
  input: glTF Id(integer)
  interpolation: enum string {LINEAR, STEP, CUBICSPLINE}
  output: glTF Id(integer)
  extensions: Extension(object)
  extras: Extras(unknown)
}
Animation(object)
{
  channels: Animation Channel(object)[]
  samplers: Animation Sampler(object)[]
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
Asset(object)
{
  copyright: string
  generator: string
  version: string
  minVersion: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
Buffer(object)
{
  uri: string
  byteLength: integer
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
Buffer View(object)
{
  buffer: glTF Id(integer)
  byteOffset: integer
  byteLength: integer
  byteStride: integer
  target: enum integer {ARRAY_BUFFER=34962, ELEMENT_ARRAY_BUFFER=34963}
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
Camera Orthographic(object)
{
  xmag: number
  ymag: number
  zfar: number
  znear: number
  extensions: Extension(object)
  extras: Extras(unknown)
}
Camera Perspective(object)
{
  aspectRatio: number
  yfov: number
  zfar: number
  znear: number
  extensions: Extension(object)
  extras: Extras(unknown)
}
Camera(object)
{
  orthographic: Camera Orthographic(object)
  perspective: Camera Perspective(object)
  type: enum string {perspective, orthographic}
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
Image(object)
{
  uri: string
  mimeType: enum string {image/jpeg, image/png}
  bufferView: glTF Id(integer)
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
Texture Info(object)
{
  index: glTF Id(integer)
  texCoord: integer
  extensions: Extension(object)
  extras: Extras(unknown)
}
Material PBR Metallic Roughness(object)
{
  baseColorFactor: number[]
  baseColorTexture: Texture Info(object)
  metallicFactor: number
  roughnessFactor: number
  metallicRoughnessTexture: Texture Info(object)
  extensions: Extension(object)
  extras: Extras(unknown)
}
Material Normal Texture Info(object)
{
  index: glTF Id(integer)
  texCoord: integer
  scale: number
  extensions: Extension(object)
  extras: Extras(unknown)
}
Material Occlusion Texture Info(object)
{
  index: glTF Id(integer)
  texCoord: integer
  strength: number
  extensions: Extension(object)
  extras: Extras(unknown)
}
Material(object)
{
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
  pbrMetallicRoughness: Material PBR Metallic Roughness(object)
  normalTexture: Material Normal Texture Info(object)
  occlusionTexture: Material Occlusion Texture Info(object)
  emissiveTexture: Texture Info(object)
  emissiveFactor: number[]
  alphaMode: enum string {OPAQUE, MASK, BLEND}
  alphaCutoff: number
  doubleSided: boolean
}
Mesh Primitive(object)
{
  attributes: object
  indices: glTF Id(integer)
  material: glTF Id(integer)
  mode: enum integer {POINTS=0, LINES=1, LINE_LOOP=2, LINE_STRIP=3, TRIANGLES=4, TRIANGLE_STRIP=5, TRIANGLE_FAN=6}
  targets: object[]
  extensions: Extension(object)
  extras: Extras(unknown)
}
Mesh(object)
{
  primitives: Mesh Primitive(object)[]
  weights: number[]
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
Node(object)
{
  camera: glTF Id(integer)
  children: glTF Id(integer)[]
  skin: glTF Id(integer)
  matrix: number[]
  mesh: glTF Id(integer)
  rotation: number[]
  scale: number[]
  translation: number[]
  weights: number[]
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
Sampler(object)
{
  magFilter: enum integer {NEAREST=9728, LINEAR=9729}
  minFilter: enum integer {NEAREST=9728, LINEAR=9729, NEAREST_MIPMAP_NEAREST=9984, LINEAR_MIPMAP_NEAREST=9985, NEAREST_MIPMAP_LINEAR=9986, LINEAR_MIPMAP_LINEAR=9987}
  wrapS: enum integer {CLAMP_TO_EDGE=33071, MIRRORED_REPEAT=33648, REPEAT=10497}
  wrapT: enum integer {CLAMP_TO_EDGE=33071, MIRRORED_REPEAT=33648, REPEAT=10497}
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
Scene(object)
{
  nodes: glTF Id(integer)[]
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
Skin(object)
{
  inverseBindMatrices: glTF Id(integer)
  skeleton: glTF Id(integer)
  joints: glTF Id(integer)[]
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
Texture(object)
{
  sampler: glTF Id(integer)
  source: glTF Id(integer)
  name: string
  extensions: Extension(object)
  extras: Extras(unknown)
}
glTF(object)
{
  extensionsUsed: string[]
  extensionsRequired: string[]
  accessors: Accessor(object)[]
  animations: Animation(object)[]
  asset: Asset(object)
  buffers: Buffer(object)[]
  bufferViews: Buffer View(object)[]
  cameras: Camera(object)[]
  images: Image(object)[]
  materials: Material(object)[]
  meshes: Mesh(object)[]
  nodes: Node(object)[]
  samplers: Sampler(object)[]
  scene: glTF Id(integer)
  scenes: Scene(object)[]
  skins: Skin(object)[]
  textures: Texture(object)[]
  extensions: Extension(object)
  extras: Extras(unknown)
}
```
