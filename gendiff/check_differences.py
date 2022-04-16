from gendiff.parsing import parse_file

from gendiff.formatters import INFERENCE_FORMATS

from gendiff.diff import find_diff


def generate_diff(first_file, second_file, format='stylish'):

    first_file_data = parse_file(first_file)
    second_file_data = parse_file(second_file)
    found_diff = find_diff(first_file_data, second_file_data)
    output_format = INFERENCE_FORMATS.get(format)

    return output_format(found_diff)
