def format_value(value, depth):
    if isinstance(value, dict):
        lines = ['{']
        indent = ' ' * (depth * 4)
        bracket_indent = ' ' * ((depth - 1) * 4)

        for key, val in value.items():
            lines.append(f'{indent}{key}: {format_value(val, depth + 1)}')

        lines.append(f'{bracket_indent}}}')
        return '\n'.join(lines)

    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'

    return str(value)


def stylish(diff, depth=1):
    lines = ['{']
    indent = ' ' * (depth * 4 - 2)
    bracket_indent = ' ' * ((depth - 1) * 4)

    for key, node in diff.items():
        status = node['status']

        if status == 'nested':
            children = stylish(node['children'], depth + 1)
            lines.append(f'{indent}  {key}: {children}')

        elif status == 'same':
            value = format_value(node['value'], depth + 1)
            lines.append(f'{indent}  {key}: {value}')

        elif status == 'added':
            value = format_value(node['value'], depth + 1)
            lines.append(f'{indent}+ {key}: {value}')

        elif status == 'deleted':
            value = format_value(node['value'], depth + 1)
            lines.append(f'{indent}- {key}: {value}')

        elif status == 'changed':
            old_value = format_value(node['old_value'], depth + 1)
            new_value = format_value(node['new_value'], depth + 1)
            lines.append(f'{indent}- {key}: {old_value}')
            lines.append(f'{indent}+ {key}: {new_value}')

    lines.append(f'{bracket_indent}}}')
    return '\n'.join(lines)