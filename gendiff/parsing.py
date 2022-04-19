"""A functions that converts the data into usable python."""

import json

import yaml

import argparse


def cli_parse():
    """Parsing CLI arguments."""

    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish')
    args = parser.parse_args()
    return args


def parse(data, format):
    """
    Accepts data and format.
    Returns a dictionary.
    """

    formats = {
        'json': json.loads,
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load
    }

    return formats.get(format)(data)
