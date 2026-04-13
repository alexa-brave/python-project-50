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