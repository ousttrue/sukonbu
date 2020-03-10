#pragma once
#include "gltf.h"
#include <tuple>

namespace gltfformat
{

struct buffer
{
    const uint8_t *p = nullptr;
    const int size = 0;

    buffer slice(int offset, int length) const
    {
        return {p + offset, length};
    }
};

static int get_type_count(AccessorType type)
{
    switch (type)
    {
    case AccessorType::SCALAR:
        return 1;
    case AccessorType::VEC2:
        return 2;
    case AccessorType::VEC3:
        return 3;
    case AccessorType::VEC4:
    case AccessorType::MAT2:
        return 4;
    case AccessorType::MAT3:
        return 9;
    case AccessorType::MAT4:
        return 16;
    }

    throw;
}

static int get_component_size(AccessorComponentType type)
{
    switch (type)
    {
    case AccessorComponentType::BYTE:
    case AccessorComponentType::UNSIGNED_BYTE:
        return 1;
    case AccessorComponentType::SHORT:
    case AccessorComponentType::UNSIGNED_SHORT:
        return 2;
    case AccessorComponentType::FLOAT:
    case AccessorComponentType::UNSIGNED_INT:
        return 4;
    }

    throw;
}

static int get_stride(const Accessor &accessor)
{
    return get_type_count(accessor.type.value()) * get_component_size(accessor.componentType.value());
}

class bin
{
    const glTF m_gltf;
    std::vector<buffer> m_buffer;

public:
    bin(const glTF &gltf, const uint8_t *glbBin, int byteLength)
        : m_gltf(gltf)
    {
        m_buffer.push_back({glbBin, byteLength});
    }

    buffer get_bytes(const BufferView &view) const
    {
        auto &buffer = m_gltf.buffers[view.buffer.value()];
        auto bytes = m_buffer[view.buffer.value()];
        return bytes
            .slice(0, buffer.byteLength.value())
            .slice(view.byteOffset.value_or(0), view.byteLength.value());
    }

    buffer get_bytes(const Accessor &accessor) const
    {
        auto &view = m_gltf.bufferViews[accessor.bufferView.value()];
        auto accessor_stride = get_stride(accessor);
        return get_bytes(view)
            .slice(accessor.byteOffset.value_or(0), accessor.count.value() * accessor_stride);
    }
};
} // namespace gltfformat
