from .formatters.json import json_format
from .formatters.plain import plain
from .formatters.stylish import stylish
from .parser import parse


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse(file1)
    data2 = parse(file2)
    diff_tree = make_diff(data1, data2)
    if format_name in (None, 'stylish'):
        result = stylish(diff_tree)
    elif format_name == 'plain':
        result = plain(diff_tree)
    elif format_name == 'json':
        result = json_format(diff_tree)
    else:
        return 'wrong format'
    return result


def make_diff(data1, data2):
    diff = {}
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    all_keys = sorted(keys1.union(keys2))
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in keys1 and key not in keys2:
            diff[key] = {
                'status': 'removed',
                'value': value1
                }
        elif key not in keys1 and key in keys2:
            diff[key] = {
                'status': 'added',
                'value': value2
                }
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {
                'status': 'nest',
                'children': make_diff(value1, value2)
                }
        elif key in keys1 and key in keys2:
            if data1[key] == data2[key]:
                diff[key] = {
                    'status': 'unchanged',
                    'value': value1
                    }
            else:
                diff[key] = {
                    'status': 'changed',
                    'old_value': value1,
                    'new_value': value2
                    }
    return diff
