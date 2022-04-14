import json
from gendiff.const import (DELETED, ADDED, NESTED, NEW, NOCHANGE,
                           NUMBER_OF_SPACES, OLD, SPACE, UNCHANGED)


def print_stylish(tree, depth=1):

    output = ['{']
    start_space, end_space = calculate_space(depth)
    for item in tree:
        type_node = item.get('type')
        key = item.get('key')
        first_value = item.get('first_value')
        second_value = item.get('second_value')
        complex = item.get('nested')

        if type_node == DELETED:
            output.append('{0}{1} {2}: {3}'.format(
                start_space, OLD, key,
                get_value(first_value, depth + 1)
            ))
        elif type_node == ADDED:
            output.append('{0}{1} {2}: {3}'.format(
                start_space, NEW, key,
                get_value(first_value, depth + 1)
            ))
        elif type_node == UNCHANGED:
            output.append('{0}{1} {2}: {3}'.format(
                start_space, NOCHANGE, key,
                get_value(first_value, depth + 1)
            ))
        elif type_node == NESTED:
            output.append('{0}{1} {2}: {3}'.format(
                start_space, NOCHANGE, key,
                print_stylish(complex, depth + 1)
            ))
        else:
            output.append('{0}{1} {2}: {3}'.format(
                start_space, OLD, key,
                get_value(first_value, depth + 1)
            ))
            output.append('{0}{1} {2}: {3}'.format(
                start_space, NEW, key,
                get_value(second_value, depth + 1)
            ))

    output.append(end_space + '}')
    return '\n'.join(output)


def calculate_space(depth):

    start_space = SPACE * (NUMBER_OF_SPACES * depth - 2)
    end_space = SPACE * (NUMBER_OF_SPACES * (depth - 1))

    return start_space, end_space


def get_value(leaf, depth):
    result = []

    start_space, end_space = calculate_space(depth)

    if isinstance(leaf, dict):
        result.append('{')
        for key, value in leaf.items():
            result.append('{0}{1} {2}: {3}'.format(
                start_space, NOCHANGE,
                key, get_value(value, depth + 1)
            ))

        result.append(end_space + '}')
    elif isinstance(leaf, str):
        result.append(str(leaf))
    else:
        result.append(json.dumps(leaf))
    return '\n'.join(result)
