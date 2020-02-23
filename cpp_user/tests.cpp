#define CATCH_CONFIG_MAIN
#include <catch.hpp>
#include <fstream>
#include <string_view>
#include <vector>
#include <sukonbu_gltf.h>


void test_gltf(const std::string &test_path)
{
    auto path = test_path;
    REQUIRE(succeeded);

    auto &mesh = storage.gltf.meshes[0];

    auto indices_view = storage.get_from_accessor(storage.gltf.accessors[mesh.primitives[0].indices]);
    REQUIRE(indices_view.valuetype == simplegltf::ValueType::UInt16);
    auto p = (const uint16_t *)indices_view.data;
    REQUIRE(0 == p[0]);
    REQUIRE(1 == p[1]);
    REQUIRE(2 == p[2]);

    auto position_view = storage.get_from_accessor(storage.gltf.accessors[mesh.primitives[0].attributes["POSITION"]]);
    REQUIRE(position_view.valuetype == simplegltf::ValueType::FloatVec3);
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
    test_gltf("gltf_Sample-Models\\2.0\\Box\\glTF-Binary\\Box.glb");
}
