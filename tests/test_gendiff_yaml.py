from gendiff.check_differences import generate_diff
import tests.outputs.output_yaml as output


def test_gendiff():
    result = generate_diff('./tests/fixtures/yaml/filepath1.yml',
                           './tests/fixtures/yaml/filepath2.yml')
    assert result == output.RIGHT_YAML
    assert result != output.WRONG_YAML
    assert result != output.WRONG1_YAML
