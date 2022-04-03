from gendiff.generator import generate_diff
import tests.output_json as output


def test_gendiff():
    result = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.json')
    assert result == output.RIGHT_JSON
    assert result != output.WRONG_JSON
    assert result != output.WRONG1_JSON
