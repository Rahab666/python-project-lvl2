from gendiff.formatters import stylish, plain, json


INFERENCE_FORMATS = {
    'stylish': stylish.print_stylish,
    'plain': plain.print_plain,
    'json': json.print_json
}
