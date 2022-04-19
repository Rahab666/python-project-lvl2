#!/usr/bin/env python3

"""Gendiff script."""

from gendiff.parsing import cli_parse

from gendiff import generate_diff


def main():
    """Print differences between two files."""

    print(generate_diff(cli_parse.first_file,
                        cli_parse.second_file,
                        cli_parse.format))


if __name__ == '__main__':
    main()
