from gendiff.core.parser import parse

#import pprint

def generate_diff(file_path1, file_path2, format='stylish'):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    diff_tree = make_diff(data1, data2)
    result = format_stylish(diff_tree)
# Begin to remove
#    print(f'file1\n')
#    pprint.pprint(data1)
#    print(f'file2\n')
#    pprint.pprint(data2) 
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

    return diff


def format_stylish(tree, depth=1):
    INDENT_STEP = 4
    lines = []
    indent = ' ' * INDENT_STEP * depth
    sing_indent = ' ' * (INDENT_STEP * depth - 2)
    closing_indent = ' ' * ((depth - 1) * INDENT_STEP)

    for key, node in tree.items():
        if node['status'] == 'nest':
            children = format_stylish(node["children"], depth + 1)
            lines.append(
                f'{indent}{key}: {children}'
            )
        elif node['status'] == 'removed':
            lines.append(
                f'{sing_indent}- {key}: {style_format(node["value"])}'
            )
        elif node['status'] == 'unchanged':
            lines.append(
                f'{indent}{key}: {style_format(node["value"])}'
            )
        elif node['status'] == 'changed':
            lines.append(
                f'{sing_indent}- {key}: {style_format(node["old_value"])}'
            )
            lines.append(
                f'{sing_indent}+ {key}: {style_format(node["new_value"])}'
            )
        elif node['status'] == 'added':
            lines.append(
                f'{sing_indent}+ {key}: {style_format(node["value"])}'
            )

    result = (
        '{\n' + '\n'.join(lines) + '\n' + f'{closing_indent}' + '}'
    )
    return result


def style_format(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    return str(value)
#    return json.dumps(value).strip(f'"')
