#!/usr/bin/env python

from argparse import ArgumentParser
from datetime import datetime


def main() -> None:
    parser = get_argument_parser()
    args = parser.parse_args()
    for file in args.files:
        fix_header(file, get_header())


def get_argument_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("files", nargs="*")
    return parser


def get_header() -> str:
    return (
        "//\n"
        f"//  Copyright © {datetime.now().year} Drinklet. All rights reserved.\n"
        "//\n"
    )


def fix_header(filename: str, header: str) -> None:
    with open(filename, "r") as inf:
        lines = inf.readlines()
    lines = strip_header(lines)
    lines = ensure_blank_line(lines)
    with open(filename, "w") as outf:
        outf.write(header)
        outf.writelines(lines)


def already_has_header(lines: list[str]) -> bool:
    return bool(lines) and lines[0].startswith("//  ")


def strip_header(lines: list[str]) -> list[str]:
    idx = 0
    for i, line in enumerate(lines):
        idx = i
        if line != "//\n" and not line.startswith("//  "):
            break
    return lines[idx:]


def ensure_blank_line(lines: list[str]) -> list[str]:
    if bool(lines) and lines[0] != "\n":
        lines = ["\n"] + lines
    return lines


if __name__ == "__main__":
    main()
