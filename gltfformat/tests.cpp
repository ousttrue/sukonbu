#define CATCH_CONFIG_MAIN
#include <gltfformat/gltf_nlohmann_json.h>
#include <fstream>
#include <string_view>
#include <vector>
#include <stdint.h>
#include <catch2/catch.hpp>

static std::vector<uint8_t> read_allbytes(const std::string &path)
{
    std::vector<uint8_t> buffer;

    // open the file for binary reading
    std::ifstream file;
    file.open(path, std::ios_base::binary);
    if (file.is_open())
    {
        // get the length of the file
        file.seekg(0, std::ios::end);
        size_t fileSize = file.tellg();
        file.seekg(0, std::ios::beg);

        // read the file
        buffer.resize(fileSize);
        file.read(reinterpret_cast<char *>(buffer.data()), fileSize);
    }

    return buffer;
}

void test_gltf(const std::string &test_path)
{
    auto path = test_path;
    auto bytes = read_allbytes(path);
    auto json_string = std::string(bytes.begin(), bytes.end());
    // parse json
    auto j = nlohmann::json::parse(json_string);
    // deserialize
    gltfformat::glTF gltf;
    j.get_to(gltf);

    auto &mesh = gltf.meshes[0];

    auto indices_accessor_index = mesh.primitives[0].indices;
    REQUIRE(indices_accessor_index.has_value());
    REQUIRE(0 == indices_accessor_index.value());
    auto indices_accessor = gltf.accessors[indices_accessor_index.value()];
    REQUIRE(indices_accessor.componentType.value() == gltfformat::AccessorComponentType::UNSIGNED_SHORT);
    REQUIRE(indices_accessor.type.value() == gltfformat::AccessorType::SCALAR);
    auto indices_view = gltf.bufferViews[indices_accessor.bufferView.value()];
    // auto p = (const uint16_t *)indices_view.data;
    // REQUIRE(0 == p[0]);
    // REQUIRE(1 == p[1]);
    // REQUIRE(2 == p[2]);

    // auto position_view = storage.get_from_accessor(storage.gltf.accessors[mesh.primitives[0].attributes["POSITION"]]);
    // REQUIRE(position_view.valuetype == simplegltf::ValueType::FloatVec3);
}

// TEST_CASE("SimpleMeshes", "[gltf]")
// {
//     test_gltf("dependencies\\glTF-Sample-Models\\2.0\\SimpleMeshes\\glTF\\SimpleMeshes.gltf");
// }

// TEST_CASE("key", "[json]")
// {
//     auto json = nlohmann::json{{}};
//     auto v = json.at("x");
//     auto a = 0;
// }

TEST_CASE("Cube", "[glb]")
{
    test_gltf("glTF-Sample-Models\\2.0\\Box\\glTF\\Box.gltf");
}
