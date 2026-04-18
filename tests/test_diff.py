import argparse
import json
from pathlib import Path

import yaml
from yaml import SafeLoader

from gendiff.formatters.formater_json import json_formater
from gendiff.formatters.formater_plain import plain_formater
from gendiff.formatters.formater_stylish import stylish
from gendiff.scripts.find_diff import build_diff, reading_files


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


# тесты перевода файлов в плоские списки
def test_parser_json():
    args = argparse.Namespace(
    first_file='tests/fixtures/file1.json',
    second_file='tests/fixtures/file2.json',
    format=None,
)
    file1_test = parser_test_json('file1.json')
    file2_test = parser_test_json('file2.json')
    reading = reading_files(args.first_file, args.second_file)
    assert (file1_test, file2_test) == reading


def test_parser_yaml():
    args = argparse.Namespace(
    first_file='tests/fixtures/file1.yaml',
    second_file='tests/fixtures/file2.yaml',
    format=None,
)
    file1_test = parser_test_yaml('file1.yaml')
    file2_test = parser_test_yaml('file2.yaml')
    reading = reading_files(args.first_file, args.second_file)
    assert (file1_test, file2_test) == reading


# тестируем сравнение двух плоских списков
def test_diff_json():
    file1 = parser_test_json('file1.json')
    file2 = parser_test_json('file2.json')
    result = read_file('expected.txt')
    diff = build_diff(file1, file2)
    assert stylish(diff) == result


def test_diff_yaml():
    file1 = parser_test_yaml('file1.yaml')
    file2 = parser_test_yaml('file2.yaml')
    result = read_file('expected.txt')  # /////
    diff = build_diff(file1, file2)
    assert stylish(diff) == result


# тестируем сравнение двух плоских списков со вложенностью
def test_diff_json_rec():
    file1 = parser_test_json('file1_rec.json')
    file2 = parser_test_json('file2_rec.json')
    result = read_file('expected_rec.txt')
    diff = build_diff(file1, file2)
    assert stylish(diff) == result


def test_diff_yaml_rec():
    file1 = parser_test_yaml('file1_rec.yaml')
    file2 = parser_test_yaml('file2_rec.yaml')
    result = read_file('expected_rec.txt')
    diff = build_diff(file1, file2)
    assert stylish(diff) == result


def test_plain_format_json():
    file1 = parser_test_json('file1_rec.json')
    file2 = parser_test_json('file2_rec.json')
    diff = build_diff(file1, file2)
    assert plain_formater(diff) == read_file('expected_plain.txt')


def test_plain_format_yaml():
    file1 = parser_test_yaml('file1_rec.yaml')
    file2 = parser_test_yaml('file2_rec.yaml')
    diff = build_diff(file1, file2)
    assert plain_formater(diff) == read_file('expected_plain.txt')


def test_json_formater():
    file1 = parser_test_json('file1_rec.json')
    file2 = parser_test_yaml('file2_rec.json')
    diff = build_diff(file1, file2)
    assert json_formater(diff) == read_file('expected_json.txt')
