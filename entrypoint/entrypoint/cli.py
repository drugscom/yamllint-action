#!/bin/env python
import argparse
import sys
from glob import glob
from os.path import isfile
from typing import List, Optional

from yamllint.config import YamlLintConfigError

from entrypoint.actions import get_input
from entrypoint.yamllint import load_conf, run


def find_files(paths: List[str]) -> List[str]:
    result: List[str] = []

    for path in paths:
        for patterns in path.splitlines():
            for pattern in patterns.split():
                for file in glob(pattern, recursive=True):
                    if isfile(file):
                        result.append(file)

    return result


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", metavar="path", nargs="*")
    args = parser.parse_args(argv)

    try:
        conf = load_conf(get_input("config"))
    except YamlLintConfigError as e:
        print(f"failed to load yamllint configuration: {e}", file=sys.stderr)
        return 1

    files = find_files(args.paths)
    if not files:
        print("No target files found", file=sys.stderr)
        return 1

    return run(files, conf)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
