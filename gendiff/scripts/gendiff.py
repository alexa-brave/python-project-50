from ..files_parser import files_parser
from ..find_diff import generate_diff


def main():
    args = files_parser()
    result = generate_diff(args.first_file, args.second_file, args.format)
    return result
