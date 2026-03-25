import json
from pathlib import Path

import yaml
from yaml import SafeLoader

from gendiff.diff import generate_diff

# from gendiff.scripts.gendiff import files_parser


# путь к фикстурам
def get_test_diff(filename):
    return Path(__file__).parent / "fixtures" / filename


# чтение файла эталона результатов .txt
def read_file(filename):
    return get_test_diff(filename).read_text()


# парсеры для тестов
def parser_test_json(filepath):
    with open(get_test_diff(filepath)) as f:
        data = json.load(f)
    return data


def parser_test_yaml(filepath):
    with open(get_test_diff(filepath)) as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data


# тестs перевода файлов в плоские списки
# def test_parser_json():
#     file1 = files_parser('file1.json')
#     file2 = files_parser('file2.json')
#     assert (file1, file2) == files_parser()


# def test_parser_yaml():
#     file1 = files_parser('file1.yaml')
#     file2 = files_parser('file2.yaml')
#     assert (file1, file2) == files_parser()


# тестируем сравнение двух плоских списков
def test_diff_json():
    file1 = parser_test_json('file1.json')
    file2 = parser_test_json('file2.json')
    result = read_file('expected.txt')
    diff = generate_diff(file1, file2)
    assert diff == result


def test_diff_yaml():
    data1 = parser_test_yaml('file1.yaml')
    data2 = parser_test_yaml('file2.yaml')
    result = read_file('expected.txt')
    assert generate_diff(data1, data2) == result
