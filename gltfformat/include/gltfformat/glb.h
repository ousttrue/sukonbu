#pragma once
#include "gltf.h"
#include <stdint.h>

namespace gltfformat
{

struct ByteReader
{
    const uint8_t *m_p;
    const uint8_t *m_end;
    ByteReader(const uint8_t *p, int byteLength)
        : m_p(p), m_end(p + byteLength)
    {
    }

    bool is_end() const
    {
        return m_p >= m_end;
    }

    template <typename T>
    T read()
    {
        auto value = *(T *)m_p;
        m_p += sizeof(T);
        return value;
    }

    void skip(int size)
    {
        m_p += size;
    }
};

struct glb
{
    struct chunk
    {
        const uint8_t *p = nullptr;
        int size = 0;
    };
    chunk json;
    chunk bin;

    bool load(const uint8_t *p, int size)
    {
        // https://github.com/KhronosGroup/glTF/blob/master/specification/2.0/README.md#glb-file-format-specification
        ByteReader reader(p, size);

        //
        // glb header
        //
        auto magic = reader.read<uint32_t>();
        if (magic != 0x46546C67)
        {
            return false;
        }

        auto version = reader.read<uint32_t>();
        if (version != 2)
        {
            return false;
        }

        auto length = reader.read<uint32_t>();
        if (length != size)
        {
            return false;
        }

        //
        // glb chunks
        //
        while (!reader.is_end())
        {
            auto chunkLength = reader.read<uint32_t>();
            auto chunkType = reader.read<uint32_t>();
            if (chunkType == 0x4E4F534A)
            {
                // JSON
                if (json.p)
                {
                    // duplicated
                    throw;
                }
                json.p = reader.m_p;
                json.size = chunkLength;
                reader.skip(chunkLength);
            }
            else if (chunkType == 0x004E4942)
            {
                // BIN
                if (bin.p)
                {
                    // duplicated
                    throw;
                }
                bin.p = reader.m_p;
                bin.size = chunkLength;
                reader.skip(chunkLength);
            }
            else
            {
                return false;
            }
        }

        return true;
    }
};

} // namespace gltfformat
