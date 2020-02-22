import sys
import pathlib
import json
import io
from typing import NamedTuple, Any, List, Dict, Optional, TextIO
from sukonbu.json_schema_parser import JsonSchemaParser
from sukonbu.generators import python, dlang, cpp
import argparse


def main():
    '''
    sukonbu.py {json_path} [--lang python] [--dst dir]
    '''
    parser = argparse.ArgumentParser(description='sukonbu.')
    parser.add_argument('json', help='target json file.')
    parser.add_argument('--lang',
                        default='python',
                        choices=['python', 'dlang', 'cpp'],
                        help='generate language.')
    parser.add_argument('--dst', help='output directory.')
    args = parser.parse_args()

    # source json path
    if not args.json:
        parser.print_help()
    path = pathlib.Path(args.json)
    if not path.exists():
        raise FileExistsError(path)

    # parse
    js_parser = JsonSchemaParser()
    js_parser.process(pathlib.Path(path))

    if args.dst:
        dst = pathlib.Path(args.dst)
        if args.lang == 'python':
            python.generate(js_parser, dst)
        elif args.lang == 'dlang':
            dlang.generate(js_parser, dst)
        elif args.lang == 'cpp':
            cpp.generate(js_parser, dst)
        else:
            raise NotImplementedError(args.lang)

    else:
        js_parser.print()


if __name__ == '__main__':
    main()
