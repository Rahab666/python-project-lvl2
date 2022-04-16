import json

from gendiff.const import (
    DELETED,
    ADDED,
    NESTED,
    CHANGED,
    TEMPLATE_ADDED,
    TEMPLATE_REMOVED,
    TEMPLATE_UPDATED
)


def print_plain(tree, path=[]):

    output = []

    for item in tree:
        type_node = item.get('type')
        key = item.get('key')
        first_value = item.get('first_value')
        second_value = item.get('second_value')
        complex = item.get('nested')

        path.append(key)

        if type_node == DELETED:
            output.append(TEMPLATE_REMOVED.format('.'.join(path)))
        elif type_node == ADDED:
            output.append(TEMPLATE_ADDED.format('.'.join(path),
                                                get_value(second_value)))

        elif type_node == CHANGED:
            output.append(TEMPLATE_UPDATED.format('.'.join(path),
                                                  get_value(first_value),
                                                  get_value(second_value)))
        elif type_node == NESTED:
            output.append(print_plain(complex, path))
        path.pop()

    return '\n'.join(output)


def get_value(value):

    if isinstance(value, str):
        result = f"'{value}'"
    elif isinstance(value, dict):
        result = '[complex value]'
    else:
        result = json.dumps(value)

    return result
