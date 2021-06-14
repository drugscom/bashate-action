#!/bin/env python
import argparse
import sys
from glob import glob
from os.path import isfile
from typing import List, Optional

from entrypoint.actions import get_input
from entrypoint.bashate import RunnerWithActionsReporter


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
    ignores = get_input("ignore")
    error = get_input("error")
    warn = get_input("warn")

    parser = argparse.ArgumentParser()
    parser.add_argument("paths", metavar="path", nargs="*")
    args = parser.parse_args(argv)

    files = find_files(args.paths)
    if not files:
        print("No target files found", file=sys.stderr)
        return 1

    run = RunnerWithActionsReporter()
    run.register_ignores(ignores)
    run.register_errors(error)
    run.register_warnings(warn)

    run.check_files(files, verbose=True)

    if run.error_count > 0:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
