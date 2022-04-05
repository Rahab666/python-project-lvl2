from gendiff.check_differences import generate_diff
import tests.outputs.output_yaml as output
from gendiff.parsing import parse_file


def test_gendiff_yaml():
    result = generate_diff('./tests/fixtures/yaml/filepath1.yml',
                           './tests/fixtures/yaml/filepath2.yml')
    assert result == output.RIGHT
    assert result != output.WRONG1
    assert result != output.WRONG2


def test_parsing_yaml():
    result = parse_file('./tests/fixtures/yaml/filepath1.yml')
    assert result == output.RIGHT1
