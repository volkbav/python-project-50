def formater(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    return str(value)


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