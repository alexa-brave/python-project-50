import json
from pathlib import Path

from gendiff.diff import generate_diff

# from gendiff.scripts.gendiff import files_parser


def get_test_diff(filename):
    return Path(__file__).parent / "fixtures" / filename


def read_file(filename):
    return get_test_diff(filename).read_text()


def parser_json(filepath):
    with open(get_test_diff(filepath)) as f:
        data = json.load(f)
    return data


def test_diff():
    file1 = parser_json('file1.json')
    file2 = parser_json('file2.json')
    result = read_file('expected.txt')
    diff = generate_diff(file1, file2)
    assert diff == result


# def test_files_parser():
#     file1 = parser('file1.json')
#     file2 = parser('file2.json')
#     assert (file1, file2) == files_parser()