import unittest
import pathlib
HERE = pathlib.Path(__file__).absolute().parent
import sukonbu


class GeneratorTest(unittest.TestCase):
    def test_parser(self) -> None:
        path = HERE.parent / 'glTF/specification/2.0/schema/glTF.schema.json'
        js_parser = sukonbu.JsonSchemaParser()
        js_parser.process(path)

        self.assertEqual(js_parser.root.get_class_name(), 'glTF')
