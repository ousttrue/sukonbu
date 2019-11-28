import sys
import pathlib
import json
import io
from typing import NamedTuple, Any, List, Dict, Optional, TextIO
from .json_schema_parser import JsonSchemaParser


def main():
    path = sys.argv[1]
    parser = JsonSchemaParser()
    parser.process(pathlib.Path(path))
    for key, js in parser.schema_map.items():
        print(js)
        print('{')
        for k, v in js.properties.items():
            print(f'  {k}: {v}')
        print('}')


if __name__ == '__main__':
    main()
