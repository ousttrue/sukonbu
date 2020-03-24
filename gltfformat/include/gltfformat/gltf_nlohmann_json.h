// this is generated by sukonbu
#pragma once
#include "gltf.h"
#include <nlohmann/json.hpp>

// partial specialization (full specialization works too)
namespace nlohmann
{
template <typename T>
struct adl_serializer<std::optional<T>>
{
    static void to_json(json &j, const std::optional<T> &opt)
    {
        if (opt.has_value())
        {
            j = *opt;
        }
    }
    static void from_json(const json &j, std::optional<T> &opt)
    {
        if (!j.is_null())
        {
            opt = j.get<T>();                               
        }
    }
};
} // namespace nlohmann

namespace gltfformat {
using nlohmann::json;

void to_json(json& j, const AccessorComponentType & p) {
}
void from_json(const json& j, AccessorComponentType& p) {
    p = (AccessorComponentType)j.get<int>();
}

void to_json(json& j, const AccessorType & p) {
}
void from_json(const json& j, AccessorType& p) {
    auto value = j.get<std::string>();
    if(value=="SCALAR")p = AccessorType::SCALAR;
    if(value=="VEC2")p = AccessorType::VEC2;
    if(value=="VEC3")p = AccessorType::VEC3;
    if(value=="VEC4")p = AccessorType::VEC4;
    if(value=="MAT2")p = AccessorType::MAT2;
    if(value=="MAT3")p = AccessorType::MAT3;
    if(value=="MAT4")p = AccessorType::MAT4;
}

void to_json(json& j, const AccessorSparseIndicesComponentType & p) {
}
void from_json(const json& j, AccessorSparseIndicesComponentType& p) {
    p = (AccessorSparseIndicesComponentType)j.get<int>();
}

void to_json(json& j, const AccessorSparseIndicesExtension & p) {
}
void from_json(const json& j, AccessorSparseIndicesExtension& p) {
}

void to_json(json& j, const AccessorSparseIndicesExtras & p) {
}
void from_json(const json& j, AccessorSparseIndicesExtras& p) {
}

void to_json(json& j, const AccessorSparseIndices & p) {
    
    
    
    
    
}
void from_json(const json& j, AccessorSparseIndices& p) {
    if(j.find("bufferView")!=j.end()) j.at("bufferView").get_to(p.bufferView);
    if(j.find("byteOffset")!=j.end()) j.at("byteOffset").get_to(p.byteOffset);
    if(j.find("componentType")!=j.end()) j.at("componentType").get_to(p.componentType);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const AccessorSparseValuesExtension & p) {
}
void from_json(const json& j, AccessorSparseValuesExtension& p) {
}

void to_json(json& j, const AccessorSparseValuesExtras & p) {
}
void from_json(const json& j, AccessorSparseValuesExtras& p) {
}

void to_json(json& j, const AccessorSparseValues & p) {
    
    
    
    
}
void from_json(const json& j, AccessorSparseValues& p) {
    if(j.find("bufferView")!=j.end()) j.at("bufferView").get_to(p.bufferView);
    if(j.find("byteOffset")!=j.end()) j.at("byteOffset").get_to(p.byteOffset);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const AccessorSparseExtension & p) {
}
void from_json(const json& j, AccessorSparseExtension& p) {
}

void to_json(json& j, const AccessorSparseExtras & p) {
}
void from_json(const json& j, AccessorSparseExtras& p) {
}

void to_json(json& j, const AccessorSparse & p) {
    
    
    
    
    
}
void from_json(const json& j, AccessorSparse& p) {
    if(j.find("count")!=j.end()) j.at("count").get_to(p.count);
    if(j.find("indices")!=j.end()) j.at("indices").get_to(p.indices);
    if(j.find("values")!=j.end()) j.at("values").get_to(p.values);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const AccessorExtension & p) {
}
void from_json(const json& j, AccessorExtension& p) {
}

void to_json(json& j, const AccessorExtras & p) {
}
void from_json(const json& j, AccessorExtras& p) {
}

void to_json(json& j, const Accessor & p) {
    
    
    
    
    
    
    
    
    
    
    
    
}
void from_json(const json& j, Accessor& p) {
    if(j.find("bufferView")!=j.end()) j.at("bufferView").get_to(p.bufferView);
    if(j.find("byteOffset")!=j.end()) j.at("byteOffset").get_to(p.byteOffset);
    if(j.find("componentType")!=j.end()) j.at("componentType").get_to(p.componentType);
    if(j.find("normalized")!=j.end()) j.at("normalized").get_to(p.normalized);
    if(j.find("count")!=j.end()) j.at("count").get_to(p.count);
    if(j.find("type")!=j.end()) j.at("type").get_to(p.type);
    if(j.find("max")!=j.end()) j.at("max").get_to(p.max);
    if(j.find("min")!=j.end()) j.at("min").get_to(p.min);
    if(j.find("sparse")!=j.end()) j.at("sparse").get_to(p.sparse);
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const AnimationChannelTargetPath & p) {
}
void from_json(const json& j, AnimationChannelTargetPath& p) {
    auto value = j.get<std::string>();
    if(value=="translation")p = AnimationChannelTargetPath::translation;
    if(value=="rotation")p = AnimationChannelTargetPath::rotation;
    if(value=="scale")p = AnimationChannelTargetPath::scale;
    if(value=="weights")p = AnimationChannelTargetPath::weights;
}

void to_json(json& j, const AnimationChannelTargetExtension & p) {
}
void from_json(const json& j, AnimationChannelTargetExtension& p) {
}

void to_json(json& j, const AnimationChannelTargetExtras & p) {
}
void from_json(const json& j, AnimationChannelTargetExtras& p) {
}

void to_json(json& j, const AnimationChannelTarget & p) {
    
    
    
    
}
void from_json(const json& j, AnimationChannelTarget& p) {
    if(j.find("node")!=j.end()) j.at("node").get_to(p.node);
    if(j.find("path")!=j.end()) j.at("path").get_to(p.path);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const AnimationChannelExtension & p) {
}
void from_json(const json& j, AnimationChannelExtension& p) {
}

void to_json(json& j, const AnimationChannelExtras & p) {
}
void from_json(const json& j, AnimationChannelExtras& p) {
}

void to_json(json& j, const AnimationChannel & p) {
    
    
    
    
}
void from_json(const json& j, AnimationChannel& p) {
    if(j.find("sampler")!=j.end()) j.at("sampler").get_to(p.sampler);
    if(j.find("target")!=j.end()) j.at("target").get_to(p.target);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const AnimationSamplerInterpolation & p) {
}
void from_json(const json& j, AnimationSamplerInterpolation& p) {
    auto value = j.get<std::string>();
    if(value=="LINEAR")p = AnimationSamplerInterpolation::LINEAR;
    if(value=="STEP")p = AnimationSamplerInterpolation::STEP;
    if(value=="CUBICSPLINE")p = AnimationSamplerInterpolation::CUBICSPLINE;
}

void to_json(json& j, const AnimationSamplerExtension & p) {
}
void from_json(const json& j, AnimationSamplerExtension& p) {
}

void to_json(json& j, const AnimationSamplerExtras & p) {
}
void from_json(const json& j, AnimationSamplerExtras& p) {
}

void to_json(json& j, const AnimationSampler & p) {
    
    
    
    
    
}
void from_json(const json& j, AnimationSampler& p) {
    if(j.find("input")!=j.end()) j.at("input").get_to(p.input);
    if(j.find("interpolation")!=j.end()) j.at("interpolation").get_to(p.interpolation);
    if(j.find("output")!=j.end()) j.at("output").get_to(p.output);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const AnimationExtension & p) {
}
void from_json(const json& j, AnimationExtension& p) {
}

void to_json(json& j, const AnimationExtras & p) {
}
void from_json(const json& j, AnimationExtras& p) {
}

void to_json(json& j, const Animation & p) {
    
    
    
    
    
}
void from_json(const json& j, Animation& p) {
    if(j.find("channels")!=j.end()) j.at("channels").get_to(p.channels);
    if(j.find("samplers")!=j.end()) j.at("samplers").get_to(p.samplers);
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const AssetExtension & p) {
}
void from_json(const json& j, AssetExtension& p) {
}

void to_json(json& j, const AssetExtras & p) {
}
void from_json(const json& j, AssetExtras& p) {
}

void to_json(json& j, const Asset & p) {
    
    
    
    
    
    
}
void from_json(const json& j, Asset& p) {
    if(j.find("copyright")!=j.end()) j.at("copyright").get_to(p.copyright);
    if(j.find("generator")!=j.end()) j.at("generator").get_to(p.generator);
    if(j.find("version")!=j.end()) j.at("version").get_to(p.version);
    if(j.find("minVersion")!=j.end()) j.at("minVersion").get_to(p.minVersion);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const BufferExtension & p) {
}
void from_json(const json& j, BufferExtension& p) {
}

void to_json(json& j, const BufferExtras & p) {
}
void from_json(const json& j, BufferExtras& p) {
}

void to_json(json& j, const Buffer & p) {
    
    
    
    
    
}
void from_json(const json& j, Buffer& p) {
    if(j.find("uri")!=j.end()) j.at("uri").get_to(p.uri);
    if(j.find("byteLength")!=j.end()) j.at("byteLength").get_to(p.byteLength);
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const BufferViewTarget & p) {
}
void from_json(const json& j, BufferViewTarget& p) {
    p = (BufferViewTarget)j.get<int>();
}

void to_json(json& j, const BufferViewExtension & p) {
}
void from_json(const json& j, BufferViewExtension& p) {
}

void to_json(json& j, const BufferViewExtras & p) {
}
void from_json(const json& j, BufferViewExtras& p) {
}

void to_json(json& j, const BufferView & p) {
    
    
    
    
    
    
    
    
}
void from_json(const json& j, BufferView& p) {
    if(j.find("buffer")!=j.end()) j.at("buffer").get_to(p.buffer);
    if(j.find("byteOffset")!=j.end()) j.at("byteOffset").get_to(p.byteOffset);
    if(j.find("byteLength")!=j.end()) j.at("byteLength").get_to(p.byteLength);
    if(j.find("byteStride")!=j.end()) j.at("byteStride").get_to(p.byteStride);
    if(j.find("target")!=j.end()) j.at("target").get_to(p.target);
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const CameraOrthographicExtension & p) {
}
void from_json(const json& j, CameraOrthographicExtension& p) {
}

void to_json(json& j, const CameraOrthographicExtras & p) {
}
void from_json(const json& j, CameraOrthographicExtras& p) {
}

void to_json(json& j, const CameraOrthographic & p) {
    
    
    
    
    
    
}
void from_json(const json& j, CameraOrthographic& p) {
    if(j.find("xmag")!=j.end()) j.at("xmag").get_to(p.xmag);
    if(j.find("ymag")!=j.end()) j.at("ymag").get_to(p.ymag);
    if(j.find("zfar")!=j.end()) j.at("zfar").get_to(p.zfar);
    if(j.find("znear")!=j.end()) j.at("znear").get_to(p.znear);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const CameraPerspectiveExtension & p) {
}
void from_json(const json& j, CameraPerspectiveExtension& p) {
}

void to_json(json& j, const CameraPerspectiveExtras & p) {
}
void from_json(const json& j, CameraPerspectiveExtras& p) {
}

void to_json(json& j, const CameraPerspective & p) {
    
    
    
    
    
    
}
void from_json(const json& j, CameraPerspective& p) {
    if(j.find("aspectRatio")!=j.end()) j.at("aspectRatio").get_to(p.aspectRatio);
    if(j.find("yfov")!=j.end()) j.at("yfov").get_to(p.yfov);
    if(j.find("zfar")!=j.end()) j.at("zfar").get_to(p.zfar);
    if(j.find("znear")!=j.end()) j.at("znear").get_to(p.znear);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const CameraType & p) {
}
void from_json(const json& j, CameraType& p) {
    auto value = j.get<std::string>();
    if(value=="perspective")p = CameraType::perspective;
    if(value=="orthographic")p = CameraType::orthographic;
}

void to_json(json& j, const CameraExtension & p) {
}
void from_json(const json& j, CameraExtension& p) {
}

void to_json(json& j, const CameraExtras & p) {
}
void from_json(const json& j, CameraExtras& p) {
}

void to_json(json& j, const Camera & p) {
    
    
    
    
    
    
}
void from_json(const json& j, Camera& p) {
    if(j.find("orthographic")!=j.end()) j.at("orthographic").get_to(p.orthographic);
    if(j.find("perspective")!=j.end()) j.at("perspective").get_to(p.perspective);
    if(j.find("type")!=j.end()) j.at("type").get_to(p.type);
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const ImageMimeType & p) {
}
void from_json(const json& j, ImageMimeType& p) {
    auto value = j.get<std::string>();
    if(value=="image/jpeg")p = ImageMimeType::imagejpeg;
    if(value=="image/png")p = ImageMimeType::imagepng;
}

void to_json(json& j, const ImageExtension & p) {
}
void from_json(const json& j, ImageExtension& p) {
}

void to_json(json& j, const ImageExtras & p) {
}
void from_json(const json& j, ImageExtras& p) {
}

void to_json(json& j, const Image & p) {
    
    
    
    
    
    
}
void from_json(const json& j, Image& p) {
    if(j.find("uri")!=j.end()) j.at("uri").get_to(p.uri);
    if(j.find("mimeType")!=j.end()) j.at("mimeType").get_to(p.mimeType);
    if(j.find("bufferView")!=j.end()) j.at("bufferView").get_to(p.bufferView);
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const MaterialExtension & p) {
}
void from_json(const json& j, MaterialExtension& p) {
}

void to_json(json& j, const MaterialExtras & p) {
}
void from_json(const json& j, MaterialExtras& p) {
}

void to_json(json& j, const TextureInfoExtension & p) {
}
void from_json(const json& j, TextureInfoExtension& p) {
}

void to_json(json& j, const TextureInfoExtras & p) {
}
void from_json(const json& j, TextureInfoExtras& p) {
}

void to_json(json& j, const TextureInfo & p) {
    
    
    
    
}
void from_json(const json& j, TextureInfo& p) {
    if(j.find("index")!=j.end()) j.at("index").get_to(p.index);
    if(j.find("texCoord")!=j.end()) j.at("texCoord").get_to(p.texCoord);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const MaterialPBRMetallicRoughnessExtension & p) {
}
void from_json(const json& j, MaterialPBRMetallicRoughnessExtension& p) {
}

void to_json(json& j, const MaterialPBRMetallicRoughnessExtras & p) {
}
void from_json(const json& j, MaterialPBRMetallicRoughnessExtras& p) {
}

void to_json(json& j, const MaterialPBRMetallicRoughness & p) {
    
    
    
    
    
    
    
}
void from_json(const json& j, MaterialPBRMetallicRoughness& p) {
    if(j.find("baseColorFactor")!=j.end()) j.at("baseColorFactor").get_to(p.baseColorFactor);
    if(j.find("baseColorTexture")!=j.end()) j.at("baseColorTexture").get_to(p.baseColorTexture);
    if(j.find("metallicFactor")!=j.end()) j.at("metallicFactor").get_to(p.metallicFactor);
    if(j.find("roughnessFactor")!=j.end()) j.at("roughnessFactor").get_to(p.roughnessFactor);
    if(j.find("metallicRoughnessTexture")!=j.end()) j.at("metallicRoughnessTexture").get_to(p.metallicRoughnessTexture);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const MaterialNormalTextureInfoExtension & p) {
}
void from_json(const json& j, MaterialNormalTextureInfoExtension& p) {
}

void to_json(json& j, const MaterialNormalTextureInfoExtras & p) {
}
void from_json(const json& j, MaterialNormalTextureInfoExtras& p) {
}

void to_json(json& j, const MaterialNormalTextureInfo & p) {
    
    
    
    
    
}
void from_json(const json& j, MaterialNormalTextureInfo& p) {
    if(j.find("index")!=j.end()) j.at("index").get_to(p.index);
    if(j.find("texCoord")!=j.end()) j.at("texCoord").get_to(p.texCoord);
    if(j.find("scale")!=j.end()) j.at("scale").get_to(p.scale);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const MaterialOcclusionTextureInfoExtension & p) {
}
void from_json(const json& j, MaterialOcclusionTextureInfoExtension& p) {
}

void to_json(json& j, const MaterialOcclusionTextureInfoExtras & p) {
}
void from_json(const json& j, MaterialOcclusionTextureInfoExtras& p) {
}

void to_json(json& j, const MaterialOcclusionTextureInfo & p) {
    
    
    
    
    
}
void from_json(const json& j, MaterialOcclusionTextureInfo& p) {
    if(j.find("index")!=j.end()) j.at("index").get_to(p.index);
    if(j.find("texCoord")!=j.end()) j.at("texCoord").get_to(p.texCoord);
    if(j.find("strength")!=j.end()) j.at("strength").get_to(p.strength);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const MaterialAlphaMode & p) {
}
void from_json(const json& j, MaterialAlphaMode& p) {
    auto value = j.get<std::string>();
    if(value=="OPAQUE")p = MaterialAlphaMode::OPAQUE;
    if(value=="MASK")p = MaterialAlphaMode::MASK;
    if(value=="BLEND")p = MaterialAlphaMode::BLEND;
}

void to_json(json& j, const Material & p) {
    
    
    
    
    
    
    
    
    
    
    
}
void from_json(const json& j, Material& p) {
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
    if(j.find("pbrMetallicRoughness")!=j.end()) j.at("pbrMetallicRoughness").get_to(p.pbrMetallicRoughness);
    if(j.find("normalTexture")!=j.end()) j.at("normalTexture").get_to(p.normalTexture);
    if(j.find("occlusionTexture")!=j.end()) j.at("occlusionTexture").get_to(p.occlusionTexture);
    if(j.find("emissiveTexture")!=j.end()) j.at("emissiveTexture").get_to(p.emissiveTexture);
    if(j.find("emissiveFactor")!=j.end()) j.at("emissiveFactor").get_to(p.emissiveFactor);
    if(j.find("alphaMode")!=j.end()) j.at("alphaMode").get_to(p.alphaMode);
    if(j.find("alphaCutoff")!=j.end()) j.at("alphaCutoff").get_to(p.alphaCutoff);
    if(j.find("doubleSided")!=j.end()) j.at("doubleSided").get_to(p.doubleSided);
}

void to_json(json& j, const MeshPrimitiveMode & p) {
}
void from_json(const json& j, MeshPrimitiveMode& p) {
    p = (MeshPrimitiveMode)j.get<int>();
}

void to_json(json& j, const MeshPrimitiveExtension & p) {
}
void from_json(const json& j, MeshPrimitiveExtension& p) {
}

void to_json(json& j, const MeshPrimitiveExtras & p) {
}
void from_json(const json& j, MeshPrimitiveExtras& p) {
}

void to_json(json& j, const MeshPrimitive & p) {
    
    
    
    
    
    
    
}
void from_json(const json& j, MeshPrimitive& p) {
    if(j.find("attributes")!=j.end()) j.at("attributes").get_to(p.attributes);
    if(j.find("indices")!=j.end()) j.at("indices").get_to(p.indices);
    if(j.find("material")!=j.end()) j.at("material").get_to(p.material);
    if(j.find("mode")!=j.end()) j.at("mode").get_to(p.mode);
    if(j.find("targets")!=j.end()) j.at("targets").get_to(p.targets);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const MeshExtension & p) {
}
void from_json(const json& j, MeshExtension& p) {
}

void to_json(json& j, const MeshExtras & p) {
}
void from_json(const json& j, MeshExtras& p) {
}

void to_json(json& j, const Mesh & p) {
    
    
    
    
    
}
void from_json(const json& j, Mesh& p) {
    if(j.find("primitives")!=j.end()) j.at("primitives").get_to(p.primitives);
    if(j.find("weights")!=j.end()) j.at("weights").get_to(p.weights);
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const NodeExtension & p) {
}
void from_json(const json& j, NodeExtension& p) {
}

void to_json(json& j, const NodeExtras & p) {
}
void from_json(const json& j, NodeExtras& p) {
}

void to_json(json& j, const Node & p) {
    
    
    
    
    
    
    
    
    
    
    
    
}
void from_json(const json& j, Node& p) {
    if(j.find("camera")!=j.end()) j.at("camera").get_to(p.camera);
    if(j.find("children")!=j.end()) j.at("children").get_to(p.children);
    if(j.find("skin")!=j.end()) j.at("skin").get_to(p.skin);
    if(j.find("matrix")!=j.end()) j.at("matrix").get_to(p.matrix);
    if(j.find("mesh")!=j.end()) j.at("mesh").get_to(p.mesh);
    if(j.find("rotation")!=j.end()) j.at("rotation").get_to(p.rotation);
    if(j.find("scale")!=j.end()) j.at("scale").get_to(p.scale);
    if(j.find("translation")!=j.end()) j.at("translation").get_to(p.translation);
    if(j.find("weights")!=j.end()) j.at("weights").get_to(p.weights);
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const SamplerMagFilter & p) {
}
void from_json(const json& j, SamplerMagFilter& p) {
    p = (SamplerMagFilter)j.get<int>();
}

void to_json(json& j, const SamplerMinFilter & p) {
}
void from_json(const json& j, SamplerMinFilter& p) {
    p = (SamplerMinFilter)j.get<int>();
}

void to_json(json& j, const SamplerWrapS & p) {
}
void from_json(const json& j, SamplerWrapS& p) {
    p = (SamplerWrapS)j.get<int>();
}

void to_json(json& j, const SamplerWrapT & p) {
}
void from_json(const json& j, SamplerWrapT& p) {
    p = (SamplerWrapT)j.get<int>();
}

void to_json(json& j, const SamplerExtension & p) {
}
void from_json(const json& j, SamplerExtension& p) {
}

void to_json(json& j, const SamplerExtras & p) {
}
void from_json(const json& j, SamplerExtras& p) {
}

void to_json(json& j, const Sampler & p) {
    
    
    
    
    
    
    
}
void from_json(const json& j, Sampler& p) {
    if(j.find("magFilter")!=j.end()) j.at("magFilter").get_to(p.magFilter);
    if(j.find("minFilter")!=j.end()) j.at("minFilter").get_to(p.minFilter);
    if(j.find("wrapS")!=j.end()) j.at("wrapS").get_to(p.wrapS);
    if(j.find("wrapT")!=j.end()) j.at("wrapT").get_to(p.wrapT);
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const SceneExtension & p) {
}
void from_json(const json& j, SceneExtension& p) {
}

void to_json(json& j, const SceneExtras & p) {
}
void from_json(const json& j, SceneExtras& p) {
}

void to_json(json& j, const Scene & p) {
    
    
    
    
}
void from_json(const json& j, Scene& p) {
    if(j.find("nodes")!=j.end()) j.at("nodes").get_to(p.nodes);
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const SkinExtension & p) {
}
void from_json(const json& j, SkinExtension& p) {
}

void to_json(json& j, const SkinExtras & p) {
}
void from_json(const json& j, SkinExtras& p) {
}

void to_json(json& j, const Skin & p) {
    
    
    
    
    
    
}
void from_json(const json& j, Skin& p) {
    if(j.find("inverseBindMatrices")!=j.end()) j.at("inverseBindMatrices").get_to(p.inverseBindMatrices);
    if(j.find("skeleton")!=j.end()) j.at("skeleton").get_to(p.skeleton);
    if(j.find("joints")!=j.end()) j.at("joints").get_to(p.joints);
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const TextureExtension & p) {
}
void from_json(const json& j, TextureExtension& p) {
}

void to_json(json& j, const TextureExtras & p) {
}
void from_json(const json& j, TextureExtras& p) {
}

void to_json(json& j, const Texture & p) {
    
    
    
    
    
}
void from_json(const json& j, Texture& p) {
    if(j.find("sampler")!=j.end()) j.at("sampler").get_to(p.sampler);
    if(j.find("source")!=j.end()) j.at("source").get_to(p.source);
    if(j.find("name")!=j.end()) j.at("name").get_to(p.name);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const glTFExtension & p) {
}
void from_json(const json& j, glTFExtension& p) {
}

void to_json(json& j, const glTFExtras & p) {
}
void from_json(const json& j, glTFExtras& p) {
}

void to_json(json& j, const glTF & p) {
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}
void from_json(const json& j, glTF& p) {
    if(j.find("extensionsUsed")!=j.end()) j.at("extensionsUsed").get_to(p.extensionsUsed);
    if(j.find("extensionsRequired")!=j.end()) j.at("extensionsRequired").get_to(p.extensionsRequired);
    if(j.find("accessors")!=j.end()) j.at("accessors").get_to(p.accessors);
    if(j.find("animations")!=j.end()) j.at("animations").get_to(p.animations);
    if(j.find("asset")!=j.end()) j.at("asset").get_to(p.asset);
    if(j.find("buffers")!=j.end()) j.at("buffers").get_to(p.buffers);
    if(j.find("bufferViews")!=j.end()) j.at("bufferViews").get_to(p.bufferViews);
    if(j.find("cameras")!=j.end()) j.at("cameras").get_to(p.cameras);
    if(j.find("images")!=j.end()) j.at("images").get_to(p.images);
    if(j.find("materials")!=j.end()) j.at("materials").get_to(p.materials);
    if(j.find("meshes")!=j.end()) j.at("meshes").get_to(p.meshes);
    if(j.find("nodes")!=j.end()) j.at("nodes").get_to(p.nodes);
    if(j.find("samplers")!=j.end()) j.at("samplers").get_to(p.samplers);
    if(j.find("scene")!=j.end()) j.at("scene").get_to(p.scene);
    if(j.find("scenes")!=j.end()) j.at("scenes").get_to(p.scenes);
    if(j.find("skins")!=j.end()) j.at("skins").get_to(p.skins);
    if(j.find("textures")!=j.end()) j.at("textures").get_to(p.textures);
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}

void to_json(json& j, const KHR_materials_unlitglTFextensionExtension & p) {
}
void from_json(const json& j, KHR_materials_unlitglTFextensionExtension& p) {
}

void to_json(json& j, const KHR_materials_unlitglTFextensionExtras & p) {
}
void from_json(const json& j, KHR_materials_unlitglTFextensionExtras& p) {
}

void to_json(json& j, const KHR_materials_unlitglTFextension & p) {
    
    
}
void from_json(const json& j, KHR_materials_unlitglTFextension& p) {
    if(j.find("extensions")!=j.end()) j.at("extensions").get_to(p.extensions);
    if(j.find("extras")!=j.end()) j.at("extras").get_to(p.extras);
}
} // end of namespace
