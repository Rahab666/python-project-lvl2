#!/usr/bin/env python
import argparse
from gendiff.methods_of_comparison.gendiff_json import generate_diff_json


def generate_diff(first_file='first_file', second_file='second_file'):
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(first_file, type=str)
    parser.add_argument(second_file, type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff_json(args.first_file, args.second_file))


if __name__ == '__generate_diff__':
    generate_diff()
