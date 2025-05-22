from gendiff.core.parser import parse

import pprint

def generate_diff(file_path1, file_path2, format=None):
    data1 = parse(file_path1.lower())
    data2 = parse(file_path2.lower())
    diff_tree = make_diff(data1, data2)
    result = flat(diff_tree)
# Begin to remove
    print(f'file1\n')
    pprint.pprint(data1)
    print(f'file2\n')
    pprint.pprint(data2) 
# End to remove
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
        elif isinstance(value1, dict) and isinstance(value2,dict):
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

    print(f'---diff---')
    pprint.pprint(diff)
    print('---')
    return diff


def flat(tree):
    result = '{'
    for key, value in tree.items():
        if value['status'] == 'removed':
            result += (
                f'\n  - {key}: {json_style_format(value["value"])}'
            )
        elif value['status'] == 'unchanged':
            result += (
                f'\n    {key}: {json_style_format(value["value"])}'
            )
        elif value['status'] == 'changed':
            result += (
                f'\n  - {key}: {json_style_format(value["old_value"])}'
            )
            result += (
                f'\n  + {key}: {json_style_format(value["new_value"])}'
            )
        elif value['status'] == 'added':
            result += (
                f'\n  + {key}: {json_style_format(value["value"])}'
            )
    result += '\n}'
    return result


def json_style_format(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    return str(value)
