from gendiff.check_differences import generate_diff
import tests.outputs.output as output
from gendiff.parsing import parse_file


def test_parsing_yaml():
    result = parse_file('./tests/fixtures/yaml/filepath1_plain.yml')
    assert result == output.RIGHT_PARSING


def test_parsing_json():
    result = parse_file('./tests/fixtures/json/file1_plain.json')
    assert result == output.RIGHT_PARSING


def test_gendiff_yaml_plain():
    result = generate_diff('./tests/fixtures/yaml/filepath1_plain.yml',
                           './tests/fixtures/yaml/filepath2_plain.yml')
    assert result == output.RIGHT_PLAIN


def test_gendiff_json_plain():
    result = generate_diff('./tests/fixtures/json/file1_plain.json',
                           './tests/fixtures/json/file2_plain.json')
    assert result == output.RIGHT_PLAIN


def test_gendiff_json_nest():
    result = generate_diff('./tests/fixtures/json/file1_nest.json',
                           './tests/fixtures/json/file2_nest.json')
    assert result == output.RIGHT_NEST


def test_gendiff_yaml_nest():
    result = generate_diff('./tests/fixtures/json/file1_nest.json',
                           './tests/fixtures/json/file2_nest.json')
    assert result == output.RIGHT_NEST
