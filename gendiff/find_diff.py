from .visual.formater_json import json_formater
from .visual.formater_plain import plain_formater
from .visual.formater_stylish import stylish


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


def generate_diff(data1, data2, format_name):
    tree = build_diff(data1, data2)
    
    if format_name == 'plain':
        return plain_formater(tree)
    elif format_name == 'json':
        return json_formater(tree)
    else:
        return stylish(tree)