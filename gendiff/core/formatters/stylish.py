from .formatters import stylish_format

INDENT_STEP = 4


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


