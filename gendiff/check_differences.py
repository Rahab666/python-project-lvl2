import copy
from gendiff.parsing import parse_file


def key_sorting(first_dict, second_dict):

    first_keys = list(first_dict.keys())
    second_keys = list(second_dict.keys())
    all_keys = copy.deepcopy(first_keys)
    first_keys_copy = copy.deepcopy(first_keys)
    second_keys_copy = copy.deepcopy(second_keys)
    all_keys.extend(second_keys_copy)
    all_keys.sort()
    equal_keys = []

    for key in first_keys_copy:
        if key in second_keys_copy:
            if first_dict[key] == second_dict[key]:
                equal_keys.append(key)
                first_keys.remove(key)
                second_keys.remove(key)
                all_keys.remove(key)
            else:
                all_keys.remove(key)
    return all_keys, first_keys, second_keys, equal_keys


def print_gendiff(sorted_keys, first_dict, second_dict):
    all_keys, first_keys, second_keys, equal_keys = sorted_keys

    output_string = '{\n'
    for key in all_keys:
        if key in first_keys:
            output_string += f"  - {key}: {first_dict[key]}\n"
        if key in second_keys:
            output_string += f"  + {key}: {second_dict[key]}\n"
        if key in equal_keys:
            output_string += f"    {key}: {first_dict[key]}\n"
    output_string += '}'
    return output_string


def generate_diff(first_file, second_file):

    first_file_data = parse_file(first_file)
    second_file_data = parse_file(second_file)

    sorted_keys = key_sorting(first_file_data, second_file_data)

    return print_gendiff(sorted_keys, first_file_data, second_file_data)
