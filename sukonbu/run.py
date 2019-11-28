import sys
import pathlib
import json
import io
from typing import NamedTuple, Any, List, Dict, Optional, TextIO
from .json_schema_parser import JsonSchemaParser


def main():
    path = sys.argv[1]
    JsonSchemaParser().process(pathlib.Path(path))


if __name__ == '__main__':
    main()
