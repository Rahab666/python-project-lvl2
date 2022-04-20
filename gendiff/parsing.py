"""A functions that converts the data into usable python."""

import json

import yaml


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
