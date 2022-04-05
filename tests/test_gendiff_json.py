from gendiff.check_differences import generate_diff
import tests.outputs.output_json as output
from gendiff.parsing import parse_file


def test_gendiff_json():
    result = generate_diff('./tests/fixtures/json/file1.json',
                           './tests/fixtures/json/file2.json')
    assert result == output.RIGHT
    assert result != output.WRONG1
    assert result != output.WRONG2


def test_parsing_json():
    result = parse_file('./tests/fixtures/json/file1.json')
    assert result == output.RIGHT1
