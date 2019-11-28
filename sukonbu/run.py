import sys
import pathlib
import json
import io
from typing import NamedTuple, Any, List, Dict, Optional, TextIO
from .json_schema import JsonSchema


def preprocess(parsed: dict, directory: pathlib.Path):
    if '$schema' in parsed:
        del parsed['$schema']

    if '$ref' in parsed:
        # replace
        path = directory / parsed['$ref']
        text = path.read_text()
        ref_parsed = json.loads(text)
        ref = preprocess(ref_parsed, path.parent)
        for k, v in ref.items():
            parsed[k] = v
        del parsed['$ref']

    if 'allOf' in parsed:
        # inherited
        path = directory / parsed['allOf'][0]['$ref']
        text = path.read_text()
        ref_parsed = json.loads(text)
        ref = preprocess(ref_parsed, path.parent)
        for k, v in ref.items():
            if k in parsed:
                if k == 'properties':
                    for pk, pv in ref[k].items():
                        parsed[k][pk] = pv
                    continue
                elif k in ['title']:
                    continue
            parsed[k] = v
        del parsed['allOf']

    for key in ['anyOf', 'not', 'oneOf']:
        if key in parsed:
            del parsed[key]

    keys = [key for key in parsed.keys()]
    for key in keys:
        if key == 'properties':
            for k, v in parsed[key].items():
                preprocess(v, directory)
        elif key == 'items':
            parsed[key] = preprocess(parsed[key], directory)
        elif key in [
                'path',
                'title',
                'type',
                'description',
                'gltf_detailedDescription',
                'gltf_webgl',
                'gltf_uriType',
                'default',
                #
                'additionalProperties',
                'minProperties',
                #
                'uniqueItems',
                'minItems',
                'maxItems',
                #
                'minimum',
                'maximum',
                'multipleOf',
                'exclusiveMinimum',
                'pattern',
                'format',
                #
                #
                'required',
                'dependencies',
        ]:
            pass
        else:
            raise Exception(f'unknown {key}')

    return parsed


def process(entry_point: pathlib.Path):
    print(entry_point)
    text = entry_point.read_text()
    parsed = json.loads(text)
    processed = preprocess(parsed, entry_point.parent)
    root = JsonSchema.from_dict(processed)
    # sio = io.StringIO()
    # print(sio.getvalue())

    for js in root.traverse():
        if js.type == 'object' and not js.additionalProperties:
            print(js)


def main():
    path = sys.argv[1]
    process(pathlib.Path(path))


if __name__ == '__main__':
    main()
