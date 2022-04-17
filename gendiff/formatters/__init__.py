"""Difference output formats."""

from gendiff.formatters import stylish, plain, json


INFERENCE_FORMATS = {
    'stylish': stylish.format,
    'plain': plain.format,
    'json': json.format
}
