import argparse
import json

import yaml
from yaml import SafeLoader

from ..diff import generate_diff


def files_parser():
    parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        dest='format',
        metavar='FORMAT',
        help='set format of output'
        )

    args = parser.parse_args()
    # print(args)
    print()
    return args


def reading_files(args):
    if args.first_file[-4:] == 'json':
        with open(args.first_file) as f:
            data1 = json.load(f)
        with open(args.second_file) as f:
            data2 = json.load(f)

    elif args.first_file[-4:] == 'yaml' or args.first_file[-3:] == 'yml':
        with open(args.first_file) as f:
            data1 = yaml.load(f, Loader=SafeLoader)
        with open(args.second_file) as f:
            data2 = yaml.load(f, Loader=SafeLoader)
    return data1, data2


def main():
    args = files_parser()
    data1, data2 = reading_files(args)
    result = generate_diff(data1, data2)

    return result
