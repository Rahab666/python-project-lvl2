def keys_dict(items):
    keys = []

    def key_append(node):
        for key, value in node.items():
            if isinstance(value, dict):
                keys.append(key)
                key_append(value)
            else:
                keys.append(key)
        return keys
    return key_append(items)


def keys_sorting(first_dict, second_dict):

    first_keys = keys_dict(first_dict)
    second_keys = keys_dict(second_dict)
    equal_keys = []

    def sort_(first_node, second_node):
        for key in first_node.keys():
            if not isinstance(first_node.get(key), dict):
                if first_node.get(key) == second_node.get(key):
                    equal_keys.append(key)
                    first_keys.remove(key)
                    second_keys.remove(key)
            else:
                sort_(first_node[key], second_node[key])
        return first_keys, second_keys, equal_keys
    return sort_(first_dict, second_dict)
