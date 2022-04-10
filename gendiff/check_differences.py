from gendiff.parsing import parse_file
from gendiff.formatters.stringify import print_gendiff


def generate_diff(first_file, second_file):

    first_file_data = parse_file(first_file)
    second_file_data = parse_file(second_file)

    return print_gendiff(first_file_data, second_file_data)
