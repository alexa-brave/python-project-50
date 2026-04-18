import json
from pathlib import Path

import yaml
from yaml import SafeLoader

from ..formatters.formater_json import json_formater
from ..formatters.formater_plain import plain_formater
from ..formatters.formater_stylish import stylish


def reading_files(path1: str, path2: str):
    suffix = Path(path1).suffix  # расширение файла

    if suffix == '.json':
        with open(path1) as f:
            data1 = json.load(f)
        with open(path2) as f:
            data2 = json.load(f)

    elif suffix == '.yaml' or suffix == '.yml':
        with open(path1) as f:
            data1 = yaml.load(f, Loader=SafeLoader)
        with open(path2) as f:
            data2 = yaml.load(f, Loader=SafeLoader)
    return data1, data2


def build_diff(data1: dict, data2: dict) -> dict:
    result = {}
    keys = sorted(data1.keys() | data2.keys())

    for key in keys:
        if key not in data1:
            result[key] = {
                'status': 'added',
                'value': data2[key],
            }
        elif key not in data2:
            result[key] = {
                'status': 'deleted',
                'value': data1[key],
            }
        else:
            value1 = data1[key]
            value2 = data2[key]

            if isinstance(value1, dict) and isinstance(value2, dict):
                result[key] = {
                    'status': 'nested',
                    'children': build_diff(value1, value2),
                }
            elif value1 == value2:
                result[key] = {
                    'status': 'same',
                    'value': value1,
                }
            else:
                result[key] = {
                    'status': 'changed',
                    'old_value': value1,
                    'new_value': value2,
                }

    return result


def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1, data2 = reading_files(filepath1, filepath2)
    tree = build_diff(data1, data2)
    
    if format_name == 'plain':
        return plain_formater(tree)
    elif format_name == 'json':
        return json_formater(tree)
    else:
        return stylish(tree)