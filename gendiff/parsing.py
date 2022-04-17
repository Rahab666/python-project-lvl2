"""A function that converts the data into usable python."""

import json

import yaml


def parse_file(file):
    """
    Checks the file format and returns a dictionary.
    """

    if file.endswith('.json'):
        output_dictionary = json.load(open(file))
    elif file.endswith('.yaml') or file.endswith('.yml'):
        output_dictionary = yaml.safe_load(open(file))

    return output_dictionary
