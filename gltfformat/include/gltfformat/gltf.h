// this is generated by sukonbu
#pragma once
#include <optional>
#include <vector>
#include <string>
#include <unordered_map>

namespace gltfformat {
enum class AccessorComponentType
{
    BYTE = 5120,
    UNSIGNED_BYTE = 5121,
    SHORT = 5122,
    UNSIGNED_SHORT = 5123,
    UNSIGNED_INT = 5125,
    FLOAT = 5126,
};

enum class AccessorType
{
    SCALAR /* = "SCALAR" */,
    VEC2 /* = "VEC2" */,
    VEC3 /* = "VEC3" */,
    VEC4 /* = "VEC4" */,
    MAT2 /* = "MAT2" */,
    MAT3 /* = "MAT3" */,
    MAT4 /* = "MAT4" */,
};

enum class AccessorSparseIndicesComponentType
{
    UNSIGNED_BYTE = 5121,
    UNSIGNED_SHORT = 5123,
    UNSIGNED_INT = 5125,
};

struct AccessorSparseIndicesExtension
{
};

struct AccessorSparseIndicesExtras
{
};

struct AccessorSparseIndices
{
    // The index of the bufferView.
    std::optional<int> bufferView;
    // The offset relative to the start of the bufferView in bytes. Must be aligned.
    std::optional<int> byteOffset;
    // The indices data type.
    std::optional<AccessorSparseIndicesComponentType> componentType;
    // Dictionary object with extension-specific objects.
    std::optional<AccessorSparseIndicesExtension> extensions;
    // Application-specific data.
    std::optional<AccessorSparseIndicesExtras> extras;
};

struct AccessorSparseValuesExtension
{
};

struct AccessorSparseValuesExtras
{
};

struct AccessorSparseValues
{
    // The index of the bufferView.
    std::optional<int> bufferView;
    // The offset relative to the start of the bufferView in bytes. Must be aligned.
    std::optional<int> byteOffset;
    // Dictionary object with extension-specific objects.
    std::optional<AccessorSparseValuesExtension> extensions;
    // Application-specific data.
    std::optional<AccessorSparseValuesExtras> extras;
};

struct AccessorSparseExtension
{
};

struct AccessorSparseExtras
{
};

struct AccessorSparse
{
    // Number of entries stored in the sparse array.
    std::optional<int> count;
    // Indices of those attributes that deviate from their initialization value.
    std::optional<AccessorSparseIndices> indices;
    // Array of size `accessor.sparse.count` times number of components storing the displaced accessor attributes pointed by `accessor.sparse.indices`.
    std::optional<AccessorSparseValues> values;
    // Dictionary object with extension-specific objects.
    std::optional<AccessorSparseExtension> extensions;
    // Application-specific data.
    std::optional<AccessorSparseExtras> extras;
};

struct AccessorExtension
{
};

struct AccessorExtras
{
};

struct Accessor
{
    // The index of the bufferView.
    std::optional<int> bufferView;
    // The offset relative to the start of the bufferView in bytes.
    std::optional<int> byteOffset;
    // The datatype of components in the attribute.
    std::optional<AccessorComponentType> componentType;
    // Specifies whether integer data values should be normalized.
    std::optional<bool> normalized;
    // The number of attributes referenced by this accessor.
    std::optional<int> count;
    // Specifies if the attribute is a scalar, vector, or matrix.
    std::optional<AccessorType> type;
    // Maximum value of each component in this attribute.
    std::vector<float> max;
    // Minimum value of each component in this attribute.
    std::vector<float> min;
    // Sparse storage of attributes that deviate from their initialization value.
    std::optional<AccessorSparse> sparse;
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<AccessorExtension> extensions;
    // Application-specific data.
    std::optional<AccessorExtras> extras;
};

enum class AnimationChannelTargetPath
{
    translation /* = "translation" */,
    rotation /* = "rotation" */,
    scale /* = "scale" */,
    weights /* = "weights" */,
};

struct AnimationChannelTargetExtension
{
};

struct AnimationChannelTargetExtras
{
};

struct AnimationChannelTarget
{
    // The index of the bufferView.
    std::optional<int> node;
    // The name of the node's TRS property to modify, or the "weights" of the Morph Targets it instantiates. For the "translation" property, the values that are provided by the sampler are the translation along the x, y, and z axes. For the "rotation" property, the values are a quaternion in the order (x, y, z, w), where w is the scalar. For the "scale" property, the values are the scaling factors along the x, y, and z axes.
    std::optional<AnimationChannelTargetPath> path;
    // Dictionary object with extension-specific objects.
    std::optional<AnimationChannelTargetExtension> extensions;
    // Application-specific data.
    std::optional<AnimationChannelTargetExtras> extras;
};

struct AnimationChannelExtension
{
};

struct AnimationChannelExtras
{
};

struct AnimationChannel
{
    // The index of the bufferView.
    std::optional<int> sampler;
    // The index of the node and TRS property that an animation channel targets.
    std::optional<AnimationChannelTarget> target;
    // Dictionary object with extension-specific objects.
    std::optional<AnimationChannelExtension> extensions;
    // Application-specific data.
    std::optional<AnimationChannelExtras> extras;
};

enum class AnimationSamplerInterpolation
{
    LINEAR /* = "LINEAR" */,
    STEP /* = "STEP" */,
    CUBICSPLINE /* = "CUBICSPLINE" */,
};

struct AnimationSamplerExtension
{
};

struct AnimationSamplerExtras
{
};

struct AnimationSampler
{
    // The index of the bufferView.
    std::optional<int> input;
    // Interpolation algorithm.
    std::optional<AnimationSamplerInterpolation> interpolation;
    // The index of the bufferView.
    std::optional<int> output;
    // Dictionary object with extension-specific objects.
    std::optional<AnimationSamplerExtension> extensions;
    // Application-specific data.
    std::optional<AnimationSamplerExtras> extras;
};

struct AnimationExtension
{
};

struct AnimationExtras
{
};

struct Animation
{
    // An array of channels, each of which targets an animation's sampler at a node's property. Different channels of the same animation can't have equal targets.
    std::vector<AnimationChannel> channels;
    // An array of samplers that combines input and output accessors with an interpolation algorithm to define a keyframe graph (but not its target).
    std::vector<AnimationSampler> samplers;
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<AnimationExtension> extensions;
    // Application-specific data.
    std::optional<AnimationExtras> extras;
};

struct AssetExtension
{
};

struct AssetExtras
{
};

struct Asset
{
    // A copyright message suitable for display to credit the content creator.
    std::string copyright;
    // Tool that generated this glTF model.  Useful for debugging.
    std::string generator;
    // The glTF version that this asset targets.
    std::string version;
    // The minimum glTF version that this asset targets.
    std::string minVersion;
    // Dictionary object with extension-specific objects.
    std::optional<AssetExtension> extensions;
    // Application-specific data.
    std::optional<AssetExtras> extras;
};

struct BufferExtension
{
};

struct BufferExtras
{
};

struct Buffer
{
    // The uri of the buffer.
    std::string uri;
    // The length of the buffer in bytes.
    std::optional<int> byteLength;
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<BufferExtension> extensions;
    // Application-specific data.
    std::optional<BufferExtras> extras;
};

enum class BufferViewTarget
{
    ARRAY_BUFFER = 34962,
    ELEMENT_ARRAY_BUFFER = 34963,
};

struct BufferViewExtension
{
};

struct BufferViewExtras
{
};

struct BufferView
{
    // The index of the bufferView.
    std::optional<int> buffer;
    // The offset into the buffer in bytes.
    std::optional<int> byteOffset;
    // The total byte length of the buffer view.
    std::optional<int> byteLength;
    // The stride, in bytes.
    std::optional<int> byteStride;
    // The target that the GPU buffer should be bound to.
    std::optional<BufferViewTarget> target;
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<BufferViewExtension> extensions;
    // Application-specific data.
    std::optional<BufferViewExtras> extras;
};

struct CameraOrthographicExtension
{
};

struct CameraOrthographicExtras
{
};

struct CameraOrthographic
{
    // The floating-point horizontal magnification of the view. Must not be zero.
    std::optional<float> xmag;
    // The floating-point vertical magnification of the view. Must not be zero.
    std::optional<float> ymag;
    // The floating-point distance to the far clipping plane. `zfar` must be greater than `znear`.
    std::optional<float> zfar;
    // The floating-point distance to the near clipping plane.
    std::optional<float> znear;
    // Dictionary object with extension-specific objects.
    std::optional<CameraOrthographicExtension> extensions;
    // Application-specific data.
    std::optional<CameraOrthographicExtras> extras;
};

struct CameraPerspectiveExtension
{
};

struct CameraPerspectiveExtras
{
};

struct CameraPerspective
{
    // The floating-point aspect ratio of the field of view.
    std::optional<float> aspectRatio;
    // The floating-point vertical field of view in radians.
    std::optional<float> yfov;
    // The floating-point distance to the far clipping plane.
    std::optional<float> zfar;
    // The floating-point distance to the near clipping plane.
    std::optional<float> znear;
    // Dictionary object with extension-specific objects.
    std::optional<CameraPerspectiveExtension> extensions;
    // Application-specific data.
    std::optional<CameraPerspectiveExtras> extras;
};

enum class CameraType
{
    perspective /* = "perspective" */,
    orthographic /* = "orthographic" */,
};

struct CameraExtension
{
};

struct CameraExtras
{
};

struct Camera
{
    // An orthographic camera containing properties to create an orthographic projection matrix.
    std::optional<CameraOrthographic> orthographic;
    // A perspective camera containing properties to create a perspective projection matrix.
    std::optional<CameraPerspective> perspective;
    // Specifies if the camera uses a perspective or orthographic projection.
    std::optional<CameraType> type;
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<CameraExtension> extensions;
    // Application-specific data.
    std::optional<CameraExtras> extras;
};

enum class ImageMimeType
{
    imagejpeg /* = "image/jpeg" */,
    imagepng /* = "image/png" */,
};

struct ImageExtension
{
};

struct ImageExtras
{
};

struct Image
{
    // The uri of the image.
    std::string uri;
    // The image's MIME type. Required if `bufferView` is defined.
    std::optional<ImageMimeType> mimeType;
    // The index of the bufferView.
    std::optional<int> bufferView;
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<ImageExtension> extensions;
    // Application-specific data.
    std::optional<ImageExtras> extras;
};

struct MaterialExtension
{
};

struct MaterialExtras
{
};

struct TextureInfoExtension
{
};

struct TextureInfoExtras
{
};

struct TextureInfo
{
    // The index of the bufferView.
    std::optional<int> index;
    // The set index of texture's TEXCOORD attribute used for texture coordinate mapping.
    std::optional<int> texCoord;
    // Dictionary object with extension-specific objects.
    std::optional<TextureInfoExtension> extensions;
    // Application-specific data.
    std::optional<TextureInfoExtras> extras;
};

struct MaterialPBRMetallicRoughnessExtension
{
};

struct MaterialPBRMetallicRoughnessExtras
{
};

struct MaterialPBRMetallicRoughness
{
    // The material's base color factor.
    std::vector<float> baseColorFactor;
    // Reference to a texture.
    std::optional<TextureInfo> baseColorTexture;
    // The metalness of the material.
    std::optional<float> metallicFactor;
    // The roughness of the material.
    std::optional<float> roughnessFactor;
    // Reference to a texture.
    std::optional<TextureInfo> metallicRoughnessTexture;
    // Dictionary object with extension-specific objects.
    std::optional<MaterialPBRMetallicRoughnessExtension> extensions;
    // Application-specific data.
    std::optional<MaterialPBRMetallicRoughnessExtras> extras;
};

struct MaterialNormalTextureInfoExtension
{
};

struct MaterialNormalTextureInfoExtras
{
};

struct MaterialNormalTextureInfo
{
    // The index of the bufferView.
    std::optional<int> index;
    // The set index of texture's TEXCOORD attribute used for texture coordinate mapping.
    std::optional<int> texCoord;
    // The scalar multiplier applied to each normal vector of the normal texture.
    std::optional<float> scale;
    // Dictionary object with extension-specific objects.
    std::optional<MaterialNormalTextureInfoExtension> extensions;
    // Application-specific data.
    std::optional<MaterialNormalTextureInfoExtras> extras;
};

struct MaterialOcclusionTextureInfoExtension
{
};

struct MaterialOcclusionTextureInfoExtras
{
};

struct MaterialOcclusionTextureInfo
{
    // The index of the bufferView.
    std::optional<int> index;
    // The set index of texture's TEXCOORD attribute used for texture coordinate mapping.
    std::optional<int> texCoord;
    // A scalar multiplier controlling the amount of occlusion applied.
    std::optional<float> strength;
    // Dictionary object with extension-specific objects.
    std::optional<MaterialOcclusionTextureInfoExtension> extensions;
    // Application-specific data.
    std::optional<MaterialOcclusionTextureInfoExtras> extras;
};

enum class MaterialAlphaMode
{
    OPAQUE /* = "OPAQUE" */,
    MASK /* = "MASK" */,
    BLEND /* = "BLEND" */,
};

struct Material
{
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<MaterialExtension> extensions;
    // Application-specific data.
    std::optional<MaterialExtras> extras;
    // A set of parameter values that are used to define the metallic-roughness material model from Physically-Based Rendering (PBR) methodology.
    std::optional<MaterialPBRMetallicRoughness> pbrMetallicRoughness;
    // Reference to a texture.
    std::optional<MaterialNormalTextureInfo> normalTexture;
    // Reference to a texture.
    std::optional<MaterialOcclusionTextureInfo> occlusionTexture;
    // Reference to a texture.
    std::optional<TextureInfo> emissiveTexture;
    // The emissive color of the material.
    std::vector<float> emissiveFactor;
    // The alpha rendering mode of the material.
    std::optional<MaterialAlphaMode> alphaMode;
    // The alpha cutoff value of the material.
    std::optional<float> alphaCutoff;
    // Specifies whether the material is double sided.
    std::optional<bool> doubleSided;
};

enum class MeshPrimitiveMode
{
    POINTS = 0,
    LINES = 1,
    LINE_LOOP = 2,
    LINE_STRIP = 3,
    TRIANGLES = 4,
    TRIANGLE_STRIP = 5,
    TRIANGLE_FAN = 6,
};

struct MeshPrimitiveExtension
{
};

struct MeshPrimitiveExtras
{
};

struct MeshPrimitive
{
    // A dictionary object, where each key corresponds to mesh attribute semantic and each value is the index of the accessor containing attribute's data.
    std::unordered_map<std::string, int> attributes;
    // The index of the bufferView.
    std::optional<int> indices;
    // The index of the bufferView.
    std::optional<int> material;
    // The type of primitives to render.
    std::optional<MeshPrimitiveMode> mode;
    // An array of Morph Targets, each  Morph Target is a dictionary mapping attributes (only `POSITION`, `NORMAL`, and `TANGENT` supported) to their deviations in the Morph Target.
    std::vector<std::unordered_map<std::string, int>> targets;
    // Dictionary object with extension-specific objects.
    std::optional<MeshPrimitiveExtension> extensions;
    // Application-specific data.
    std::optional<MeshPrimitiveExtras> extras;
};

struct MeshExtension
{
};

struct MeshExtras
{
};

struct Mesh
{
    // An array of primitives, each defining geometry to be rendered with a material.
    std::vector<MeshPrimitive> primitives;
    // Array of weights to be applied to the Morph Targets.
    std::vector<float> weights;
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<MeshExtension> extensions;
    // Application-specific data.
    std::optional<MeshExtras> extras;
};

struct NodeExtension
{
};

struct NodeExtras
{
};

struct Node
{
    // The index of the bufferView.
    std::optional<int> camera;
    // The indices of this node's children.
    std::vector<int> children;
    // The index of the bufferView.
    std::optional<int> skin;
    // A floating-point 4x4 transformation matrix stored in column-major order.
    std::vector<float> matrix;
    // The index of the bufferView.
    std::optional<int> mesh;
    // The node's unit quaternion rotation in the order (x, y, z, w), where w is the scalar.
    std::vector<float> rotation;
    // The node's non-uniform scale, given as the scaling factors along the x, y, and z axes.
    std::vector<float> scale;
    // The node's translation along the x, y, and z axes.
    std::vector<float> translation;
    // The weights of the instantiated Morph Target. Number of elements must match number of Morph Targets of used mesh.
    std::vector<float> weights;
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<NodeExtension> extensions;
    // Application-specific data.
    std::optional<NodeExtras> extras;
};

enum class SamplerMagFilter
{
    NEAREST = 9728,
    LINEAR = 9729,
};

enum class SamplerMinFilter
{
    NEAREST = 9728,
    LINEAR = 9729,
    NEAREST_MIPMAP_NEAREST = 9984,
    LINEAR_MIPMAP_NEAREST = 9985,
    NEAREST_MIPMAP_LINEAR = 9986,
    LINEAR_MIPMAP_LINEAR = 9987,
};

enum class SamplerWrapS
{
    CLAMP_TO_EDGE = 33071,
    MIRRORED_REPEAT = 33648,
    REPEAT = 10497,
};

enum class SamplerWrapT
{
    CLAMP_TO_EDGE = 33071,
    MIRRORED_REPEAT = 33648,
    REPEAT = 10497,
};

struct SamplerExtension
{
};

struct SamplerExtras
{
};

struct Sampler
{
    // Magnification filter.
    std::optional<SamplerMagFilter> magFilter;
    // Minification filter.
    std::optional<SamplerMinFilter> minFilter;
    // s wrapping mode.
    std::optional<SamplerWrapS> wrapS;
    // t wrapping mode.
    std::optional<SamplerWrapT> wrapT;
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<SamplerExtension> extensions;
    // Application-specific data.
    std::optional<SamplerExtras> extras;
};

struct SceneExtension
{
};

struct SceneExtras
{
};

struct Scene
{
    // The indices of each root node.
    std::vector<int> nodes;
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<SceneExtension> extensions;
    // Application-specific data.
    std::optional<SceneExtras> extras;
};

struct SkinExtension
{
};

struct SkinExtras
{
};

struct Skin
{
    // The index of the bufferView.
    std::optional<int> inverseBindMatrices;
    // The index of the bufferView.
    std::optional<int> skeleton;
    // Indices of skeleton nodes, used as joints in this skin.
    std::vector<int> joints;
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<SkinExtension> extensions;
    // Application-specific data.
    std::optional<SkinExtras> extras;
};

struct TextureExtension
{
};

struct TextureExtras
{
};

struct Texture
{
    // The index of the bufferView.
    std::optional<int> sampler;
    // The index of the bufferView.
    std::optional<int> source;
    // The user-defined name of this object.
    std::string name;
    // Dictionary object with extension-specific objects.
    std::optional<TextureExtension> extensions;
    // Application-specific data.
    std::optional<TextureExtras> extras;
};

struct glTFExtension
{
};

struct glTFExtras
{
};

struct glTF
{
    // Names of glTF extensions used somewhere in this asset.
    std::vector<std::string> extensionsUsed;
    // Names of glTF extensions required to properly load this asset.
    std::vector<std::string> extensionsRequired;
    // An array of accessors.
    std::vector<Accessor> accessors;
    // An array of keyframe animations.
    std::vector<Animation> animations;
    // Metadata about the glTF asset.
    std::optional<Asset> asset;
    // An array of buffers.
    std::vector<Buffer> buffers;
    // An array of bufferViews.
    std::vector<BufferView> bufferViews;
    // An array of cameras.
    std::vector<Camera> cameras;
    // An array of images.
    std::vector<Image> images;
    // An array of materials.
    std::vector<Material> materials;
    // An array of meshes.
    std::vector<Mesh> meshes;
    // An array of nodes.
    std::vector<Node> nodes;
    // An array of samplers.
    std::vector<Sampler> samplers;
    // The index of the bufferView.
    std::optional<int> scene;
    // An array of scenes.
    std::vector<Scene> scenes;
    // An array of skins.
    std::vector<Skin> skins;
    // An array of textures.
    std::vector<Texture> textures;
    // Dictionary object with extension-specific objects.
    std::optional<glTFExtension> extensions;
    // Application-specific data.
    std::optional<glTFExtras> extras;
};
} // end of namespace
