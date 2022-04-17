"""Gendiff tests"""

from gendiff.check_differences import generate_diff

from tests.fixtures import output

from gendiff.parsing import parse_file


def test_parsing_yaml():
    result = parse_file('./tests/fixtures/yaml/filepath1_plain.yml')
    assert result == output.RIGHT_PARSING


def test_parsing_json():
    result = parse_file('./tests/fixtures/json/file1_plain.json')
    assert result == output.RIGHT_PARSING


def test_format():
    result = generate_diff('./tests/fixtures/yaml/filepath1_plain.yml',
                           './tests/fixtures/yaml/filepath2_plain.yml',
                           'wrong_format')
    assert result == output.FALSE_FORMAT


def test_default():
    result = generate_diff('./tests/fixtures/yaml/filepath1_plain.yml',
                           './tests/fixtures/yaml/filepath2_plain.yml')
    assert result == output.RIGHT_SIMPLE


def test_gendiff_yaml_simple():
    result = generate_diff('./tests/fixtures/yaml/filepath1_plain.yml',
                           './tests/fixtures/yaml/filepath2_plain.yml',
                           'stylish')
    assert result == output.RIGHT_SIMPLE


def test_gendiff_json_simple():
    result = generate_diff('./tests/fixtures/json/file1_plain.json',
                           './tests/fixtures/json/file2_plain.json',
                           'stylish')
    assert result == output.RIGHT_SIMPLE


def test_gendiff_json_stylish():
    result = generate_diff('./tests/fixtures/json/file1_nest.json',
                           './tests/fixtures/json/file2_nest.json',
                           'stylish')
    assert result == output.RIGHT_STYLISH


def test_gendiff_yaml_stylish():
    result = generate_diff('./tests/fixtures/yaml/filepath1_nest.yml',
                           './tests/fixtures/yaml/filepath2_nest.yml',
                           'stylish')
    assert result == output.RIGHT_STYLISH


def test_gendiff_json_plain():
    result = generate_diff('./tests/fixtures/json/file1_nest.json',
                           './tests/fixtures/json/file2_nest.json',
                           'plain')
    assert result == output.RIGHT_PLAIN


def test_gendiff_yaml_plain():
    result = generate_diff('./tests/fixtures/yaml/filepath1_nest.yml',
                           './tests/fixtures/yaml/filepath2_nest.yml',
                           'plain')
    assert result == output.RIGHT_PLAIN


def test_gendiff_json_json():
    result = generate_diff('./tests/fixtures/json/file1_nest.json',
                           './tests/fixtures/json/file2_nest.json',
                           'json')
    assert result == output.RIGHT_JSON


def test_gendiff_yaml_json():
    result = generate_diff('./tests/fixtures/yaml/filepath1_nest.yml',
                           './tests/fixtures/yaml/filepath2_nest.yml',
                           'json')
    assert result == output.RIGHT_JSON
