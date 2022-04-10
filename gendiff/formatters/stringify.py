from gendiff.diff import key_sorting


def print_gendiff(first_dict, second_dict):
    all_keys, first_keys, second_keys, equal_keys = key_sorting(first_dict,
                                                                second_dict)

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
