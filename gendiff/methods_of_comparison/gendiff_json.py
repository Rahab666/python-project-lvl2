import json
import copy


def generate_diff_json(first_file, second_file):

    first_file_data = json.load(open(first_file))
    second_file_data = json.load(open(second_file))

    first_keys = list(first_file_data.keys())
    second_keys = list(second_file_data.keys())
    first_keys_copy = copy.deepcopy(first_keys)
    first_keys_copy_ = copy.deepcopy(first_keys)
    second_keys_copy = copy.deepcopy(second_keys)
    first_keys_copy.extend(second_keys_copy)
    first_keys_copy.sort()
    equal_keys = []

    for key in first_keys_copy_:
        if key in second_keys:
            if first_file_data[key] == second_file_data[key]:
                equal_keys.append(key)
                first_keys.remove(key)
                second_keys.remove(key)
                first_keys_copy.remove(key)
            else:
                first_keys_copy.remove(key)

    output = '{\n'
    for k in first_keys_copy:
        if k in first_keys:
            output += f"  - {k} : {first_file_data[k]}\n"
        if k in second_keys:
            output += f"  + {k} : {second_file_data[k]}\n"
        if k in equal_keys:
            output += f"    {k} : {first_file_data[k]}\n"
    return output + '}'
