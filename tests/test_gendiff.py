"""Gendiff tests"""

from gendiff import generate_diff
import pytest

from tests.fixtures import output


@pytest.mark.parametrize("first_file, second_file, expected_output, format", [
    (
        './tests/fixtures/yaml/filepath1_plain.yml',
        './tests/fixtures/yaml/filepath2_plain.yml',
        output.FALSE_FORMAT,
        'wrong_format'
    ),
    (
        './tests/fixtures/yaml/filepath1_plain.yml',
        './tests/fixtures/yaml/filepath2_plain.yml',
        output.RIGHT_SIMPLE,
        'stylish'
    ),
    (
        './tests/fixtures/json/file1_plain.json',
        './tests/fixtures/json/file2_plain.json',
        output.RIGHT_SIMPLE,
        'stylish'
    ),
    (
        './tests/fixtures/json/file1_nest.json',
        './tests/fixtures/json/file2_nest.json',
        output.RIGHT_STYLISH,
        'stylish'
    ),
    (
        './tests/fixtures/yaml/filepath1_nest.yml',
        './tests/fixtures/yaml/filepath2_nest.yml',
        output.RIGHT_STYLISH,
        'stylish'
    ),
    (
        './tests/fixtures/json/file1_nest.json',
        './tests/fixtures/json/file2_nest.json',
        output.RIGHT_PLAIN,
        'plain'
    ),
    (
        './tests/fixtures/yaml/filepath1_nest.yml',
        './tests/fixtures/yaml/filepath2_nest.yml',
        output.RIGHT_PLAIN,
        'plain'
    ),
    (
        './tests/fixtures/json/file1_nest.json',
        './tests/fixtures/json/file2_nest.json',
        output.RIGHT_JSON,
        'json'
    ),
    (
        './tests/fixtures/yaml/filepath1_nest.yml',
        './tests/fixtures/yaml/filepath2_nest.yml',
        output.RIGHT_JSON,
        'json'
    ),
])
def test_gendiff(first_file, second_file, expected_output, format):
    assert generate_diff(first_file, second_file, format) == expected_output
