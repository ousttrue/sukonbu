import unittest
import pathlib
import json
import os
from generated.python import sukonbu_gltf
GLTF_SAMPLE_MODLES = pathlib.Path(
    os.getenv('GLTF_SAMPLE_MODELS'))  # type: ignore
HERE = pathlib.Path(__file__).absolute().parent


class SukonbuGltfTest(unittest.TestCase):
    def test_read(self) -> None:
        path = GLTF_SAMPLE_MODLES / "2.0/Avocado/glTF/Avocado.gltf"
        # print(gltf, gltf.exists())
        with open(path) as r:
            json_bytes = r.read()
        json_dict = json.loads(json_bytes)

        gltf = sukonbu_gltf.glTF.from_dict(json_dict)

        export = gltf.to_dict()

        self.assertEqual(json_dict, export)

        self.assertEqual(sukonbu_gltf.AccessorComponentType.FLOAT,
                         gltf.accessors[0].componentType)


if __name__ == '__main__':
    unittest.main()
