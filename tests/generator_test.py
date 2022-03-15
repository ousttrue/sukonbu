from sukonbu.json_schema_parser import JsonSchemaParser
import unittest
import pathlib
HERE = pathlib.Path(__file__).absolute().parent
import sukonbu


def parse_gltf_schema() -> sukonbu.JsonSchemaParser:
    path = HERE.parent / 'glTF/specification/2.0/schema/glTF.schema.json'
    js_parser = sukonbu.JsonSchemaParser()
    js_parser.process(path)

    # extensions
    ex_path = path.parent.parent.parent.parent / 'extensions/2.0/Khronos/KHR_materials_unlit/schema/gltf.KHR_materials_unlit.schema.json'
    ex_parser = sukonbu.JsonSchemaParser(path.parent)
    ex_parser.process(ex_path)
    js_parser.root.set('materials[].extensions.KHR_materials_unlit', ex_parser)

    # some extension
    some = sukonbu.JsonSchemaParser()
    some.root = sukonbu.JsonSchema(
        type='object',
        title='SomeExtension',
        properties={'number': sukonbu.JsonSchema(type='int', title='number')})
    js_parser.root.set('extensions.SOME_EXTENSION', some)

    # extras
    meshTargetNames = sukonbu.JsonSchemaParser()
    meshTargetNames.root = sukonbu.JsonSchema(
        type='array',
        title='meshTargetNames',
        items=sukonbu.JsonSchema(type='str'))
    js_parser.root.set('meshes[].extras.targetNames', meshTargetNames)

    primTargetNames = sukonbu.JsonSchemaParser()
    primTargetNames.root = sukonbu.JsonSchema(
        type='array',
        title='primTargetNames',
        items=sukonbu.JsonSchema(type='str'))
    js_parser.root.set('meshes[].primitives[].extras.targetNames', meshTargetNames)

    return js_parser


class GeneratorTest(unittest.TestCase):
    def test_or(self) -> None:
        self.assertEqual(1, False or 1)
        self.assertEqual(True, True or 1)

    def test_parser(self) -> None:
        js_parser = parse_gltf_schema()

        #
        # test
        #
        root = js_parser.root
        if not root:
            raise Exception()
        self.assertEqual(root.title, 'glTF')
        self.assertEqual(root['extensions'].title, 'Extension')
        self.assertEqual(
            root['extensions']['SOME_EXTENSION'].root.title,
            'SomeExtension')
