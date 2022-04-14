from gendiff.parsing import parse_file
from gendiff.formatters.stylish import print_stylish
from gendiff.diff import find_diff


def generate_diff(first_file, second_file):

    first_file_data = parse_file(first_file)
    second_file_data = parse_file(second_file)
    found_diff = find_diff(first_file_data, second_file_data)

    return print_stylish(found_diff)
