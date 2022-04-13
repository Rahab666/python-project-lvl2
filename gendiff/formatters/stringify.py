from gendiff.diff import keys_sorting
import copy


def print_gendiff(first_dict, second_dict):
    first_keys, second_keys, equal_keys = keys_sorting(first_dict, second_dict)

    def make_output(first_node, second_node, depth=1):
        first_node_copy = copy.deepcopy(first_node)
        second_node_copy = copy.deepcopy(second_node)
        output = []
        correct_depth_1 = depth * '   '
        correct_depth_2 = depth * '  '
        keys_node = list(first_node_copy.keys() | second_node_copy.keys())
        keys_node.sort()
        for key in keys_node:
            if isinstance(first_node.get(key), dict):
                output.extend([
                  f'{correct_depth_1}  {key}: {{',
                  make_output(first_node[key], second_node[key], depth+1),
                  f'{correct_depth_1}}}',
                ])
            else:
                if key in first_keys:
                    output.append("  {0}- {1}: {2}".format(correct_depth_2,
                                                           key,
                                                           first_node[key]))
                if key in second_keys:
                    output.append("  {0}+ {1}: {2}".format(correct_depth_2,
                                                           key,
                                                           second_node[key]))
                if key in equal_keys:
                    output.append("  {0}  {1}: {2}".format(correct_depth_2,
                                                           key,
                                                           first_node[key]))
        if depth == 1:
            output = ['{'] + output + ['}']
        return '\n'.join(output)
    return make_output(first_dict, second_dict)
