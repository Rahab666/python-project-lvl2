import copy


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
