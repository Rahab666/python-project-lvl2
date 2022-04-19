#!/usr/bin/env python3

"""Gendiff script."""

from gendiff.parsing import cli_parse

from gendiff import generate_diff


def main():
    """Print differences between two files."""

    args = cli_parse()

    print(generate_diff(args.first_file,
                        args.second_file,
                        args.format))


if __name__ == '__main__':
    main()
