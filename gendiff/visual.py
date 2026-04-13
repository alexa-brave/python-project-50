
def format_value(value, depth=0):
    if depth > 0:  # глубина появляется только при stylish формате
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
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict) or isinstance(value, list):
        value = '[complex value]'
    elif isinstance(value, str) and depth == 0:
        return f"\'{value}\'"

    return value


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
            value = str(format_value(node['value'], depth + 1))
            lines.append(f'{indent}  {key}: {value}')

        elif status == 'added':
            value = str(format_value(node['value'], depth + 1))
            lines.append(f'{indent}+ {key}: {value}')

        elif status == 'deleted':
            value = str(format_value(node['value'], depth + 1))
            lines.append(f'{indent}- {key}: {value}')

        elif status == 'changed':
            old_value = str(format_value(node['old_value'], depth + 1))
            new_value = str(format_value(node['new_value'], depth + 1))
            lines.append(f'{indent}- {key}: {old_value}')
            lines.append(f'{indent}+ {key}: {new_value}')

    lines.append(f'{bracket_indent}}}')
    return '\n'.join(lines)


def plain_formater(diff):
    result: list = []
    path: list = []

    def inner(any_arg):
        for key, node in any_arg.items():
            status = node['status']
            path.append(key)  # добавляем ключ в путь
            
            value = format_value(node.get('value'))
            old_value = format_value(node.get('old_value'))
            new_value = format_value(node.get('new_value'))

            # logic
            if status == 'nested':
                inner(node['children'])  # recursion
            if status == 'added':
                result.append(f"Property '{'.'.join(path)}' was added with value: {value}")  # noqa: E501
            elif status == 'deleted':
                result.append(f"Property '{'.'.join(path)}' was removed")
            elif status == 'changed':
                result.append(f"Property '{'.'.join(path)}' was updated. From {old_value} to {new_value}")  # noqa: E501
            path.remove(key)  # удаляем ключ из пути
    
    inner(diff)
    return '\n'.join(result)