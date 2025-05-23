from .formatters import format_plain_value


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