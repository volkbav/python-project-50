from gendiff.core.parser import parse

# import pprint


INDENT_STEP = 4


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse(file1)
    data2 = parse(file2)
    diff_tree = make_diff(data1, data2)
    if format_name in (None, 'stylish'):
        result = stylish(diff_tree)
    elif format_name == 'plain':
        result = plain(diff_tree)
    else:
        return 'wrong format'
# Begin to remove
    
#    print(f'file1\n')
#    pprint.pprint(data1)
#    print(f'file2\n')
#    pprint.pprint(data2) 
#    print('---tree---')
#    pprint.pprint(diff_tree)
#    return None
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
            value = stylish_format(node["value"], depth)
            lines.append(
                f'{sign_indent}- {key}: {value}'
            )
        elif node['status'] == 'unchanged':
            lines.append(
                f'{indent}{key}: {stylish_format(node["value"], depth)}'
            )
        elif node['status'] == 'changed':
            old_value = stylish_format(node["old_value"], depth)
            new_value = stylish_format(node["new_value"], depth)
            lines.append(
                f'{sign_indent}- {key}: {old_value}'
            )
            lines.append(
                f'{sign_indent}+ {key}: {new_value}'
            )
        elif node['status'] == 'added':
            lines.append(
                f'{sign_indent}+ {key}: {stylish_format(node["value"], depth)}'
            )
    result = (
        '{\n' + '\n'.join(lines) + '\n' + f'{closing_indent}' + '}'
    )
    return result


def stylish_format(value, depth=1):
    INDENT_STEP = 4
    if isinstance(value, dict):
        indent = ' ' * INDENT_STEP * (depth + 1)
        closing_indent = ' ' * INDENT_STEP * depth
        lines = []
        for k, v in value.items():
            lines.append(f'{indent}{k}: {stylish_format(v, depth + 1)}')
        return '{{\n{}\n{}}}'.format('\n'.join(lines), closing_indent)
    return formater(value)


def formater(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    return str(value)


def plain(tree, parent=''):
    lines = []
    for key, node in tree.items():
        full_key = f"{parent}{key}"
        status = node.get('status')
        
        if status == "nest":
            children = node.get('children')
            lines.extend(plain(children, f'{full_key}.').split('\n'))

        elif status == 'added':
            value = format_plain_value(node.get('value'))
            lines.append(f"Property '{full_key}' was added with value: {value}")
        elif status == 'removed':
            lines.append(f"Property '{full_key}' was removed")
        elif status == 'changed':
            old_value = format_plain_value(node.get('old_value'))
            new_value = format_plain_value(node.get('new_value'))
            line = (
                f"Property '{full_key}' was updated."
            )
            lines.append(
                f"{line} From {old_value} to {new_value}"
            )

    return '\n'.join(filter(None, lines))


def format_plain_value(val):
    if isinstance(val, dict):
        return "[complex value]"
    elif isinstance(val, bool):
        return str(val).lower()
    elif val is None:
        return "null"
    elif isinstance(val, str):
        return f"'{val}'"
    return str(val)
