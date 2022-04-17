"""Function to check if there are differences between files."""

from gendiff.parsing import parse_file

from gendiff.formatters import INFERENCE_FORMATS

from gendiff.diff import find_diff


def generate_diff(first_file, second_file, format_name='stylish'):
    """
    Checking and generating differences between two files.
    The argument first_file is path to first file.
    The argument second_file is path to second file.
    The argument format_name is difference output format.
    """

    first_file_data = parse_file(first_file)
    second_file_data = parse_file(second_file)

    found_diff = find_diff(first_file_data, second_file_data)
    output_format = INFERENCE_FORMATS.get(format_name)

    if not output_format:
        return 'The format is not supported'

    return output_format(found_diff)
