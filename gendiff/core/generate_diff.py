from gendiff.core.parse import parse_json


def generate_diff(file_path1, file_path2, format=None):
    first_file_content = parse_json(file_path1)
    second_file_content = parse_json(file_path2)
    diff_tree = make_diff(first_file_content, second_file_content)
    result = flat(diff_tree)
    return result


def make_diff(file_data1, file_data2):
    diff = {}
    keys1 = set(file_data1.keys())
    keys2 = set(file_data2.keys())
    all_keys = sorted(keys1.union(keys2))
    for key in all_keys:
        if key in keys1 and key not in keys2:
            diff[key] = {
                'status': 'removed',
                'value': file_data1[key]
            }
        elif key in keys1 and key in keys2:
            if file_data1[key] == file_data2[key]:
                diff[key] = {
                    'status': 'unchanged',
                    'value': file_data1[key]
                    }
            else:
                diff[key] = {
                    'status': 'changed',
                    'old_value': file_data1[key],
                    'new_value': file_data2[key]
                }
        elif key not in keys1 and key in keys2:
            diff[key] = {
                'status': 'added',
                'value': file_data2[key]
            }
    return diff
            

def flat(tree):
    result = '{'
    for key, value in tree.items():
        if value['status'] == 'removed':
            result += (
                f'\n  - {key} : {value['value']}'
            )
        elif value['status'] == 'unchanged':
            result += (
                f'\n    {key} : {value['value']}'
            )
        elif value['status'] == 'changed':
            result += (
                f'\n  - {key} : {value['old_value']}'
            )
            result += (
                f'\n  + {key} : {value['new_value']}'
            )
        elif value['status'] == 'added':
            result += (
                f'\n  + {key} : {value['value']}'
            )
    result += '\n}'
    return result