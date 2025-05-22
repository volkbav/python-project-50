from gendiff.core.parser import parse



INDENT_STEP = 4


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse(file1)
    data2 = parse(file2)
    diff_tree = make_diff(data1, data2)
    if format_name in (None, 'stylish'):
        result = stylish(diff_tree)
    else:
        return 'wrong format'
# Begin to remove
    import pprint
#    print(f'file1\n')
#    pprint.pprint(data1)
#    print(f'file2\n')
#    pprint.pprint(data2) 
    print('tree')
    pprint.pprint(diff_tree)
    return None
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


def stylish(tree, depth=1):
    lines = []
    indent = ' ' * INDENT_STEP * depth
    sign_indent = ' ' * (INDENT_STEP * depth - 2)
    closing_indent = ' ' * ((depth - 1) * INDENT_STEP)

    for key, node in tree.items():
        if node['status'] == 'nest':
            children = stylish(node["children"], depth + 1)
            lines.append(
                f'{indent}{key}: {children}'
                )
        elif node['status'] == 'removed':
            lines.append(
                f'{sign_indent}- {key}: {style_format(node["value"], depth)}'
                )
        elif node['status'] == 'unchanged':
            lines.append(
                f'{indent}{key}: {style_format(node["value"], depth)}'
                )
        elif node['status'] == 'changed':
            lines.append(
                f'{sign_indent}- {key}: {
                    style_format(node["old_value"], depth)
                    }'
                )
            lines.append(
                f'{sign_indent}+ {key}: {
                    style_format(node["new_value"], depth)
                    }'
                )
        elif node['status'] == 'added':
            lines.append(
                f'{sign_indent}+ {key}: {
                    style_format(node["value"], depth)
                    }'
                )
    result = (
        '{\n' + '\n'.join(lines) + '\n' + f'{closing_indent}' + '}'
        )
    return result


def style_format(value, depth=1):
    INDENT_STEP = 4
    if isinstance(value, dict):
        indent = ' ' * INDENT_STEP * (depth + 1)
        closing_indent = ' ' * INDENT_STEP * depth
        lines = []
        for k, v in value.items():
            lines.append(f'{indent}{k}: {style_format(v, depth + 1)}')
        return '{{\n{}\n{}}}'.format('\n'.join(lines), closing_indent)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)

