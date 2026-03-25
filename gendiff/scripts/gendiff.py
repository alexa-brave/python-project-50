import json

import yaml
from yaml import SafeLoader

from ..diff import generate_diff
from ..files_parser import files_parser


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
