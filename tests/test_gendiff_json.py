from gendiff.check_differences import generate_diff
import tests.outputs.output_json as output


def test_gendiff():
    result = generate_diff('./tests/fixtures/json/file1.json',
                           './tests/fixtures/json/file2.json')
    assert result == output.RIGHT_JSON
    assert result != output.WRONG_JSON
    assert result != output.WRONG1_JSON
