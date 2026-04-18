from .value_format import format_value


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