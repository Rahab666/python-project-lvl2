import json
import yaml


def parse_file(file):

    if file.endswith('.json'):
        output_file = json.load(open(file))
    elif file.endswith('.yaml') or file.endswith('.yml'):
        output_file = yaml.safe_load(open(file))

    return output_file
