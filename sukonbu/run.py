import sys
import pathlib
import json
import io
from typing import NamedTuple, Any, List, Dict, Optional, TextIO
from .json_schema_parser import JsonSchemaParser
from .generators import py
import argparse


def main():
    parser = argparse.ArgumentParser(description='sukonbu.')
    parser.add_argument('json', type=str, help='target json file.')
    parser.add_argument('--dst', type=str, help='output directory.')
    args = parser.parse_args()
    if not args.json:
        parser.print_help()

    path = pathlib.Path(args.json)
    if not path.exists():
        raise FileExistsError(path)

    # parse
    js_parser = JsonSchemaParser()
    js_parser.process(pathlib.Path(path))

    if args.dst:
        py.generate(js_parser, pathlib.Path(args.dst))

    else:
        js_parser.print()


if __name__ == '__main__':
    main()
