def generate_diff(file1, file2) -> str:  # noqa: C901

    keys = sorted(file1.keys() | file2.keys())
    strings = ['{']
    
    for key in keys:
        if key in file1 and key in file2:
            if isinstance(file1[key], bool) or isinstance(file2[key], bool):
                value1 = str(file1[key]).lower()
                value2 = str(file2[key]).lower()
            else:
                value1 = file1[key]
                value2 = file2[key]
        elif key not in file2:
            if isinstance(file1[key], bool):
                value = str(file1[key]).lower()
            else:
                value = file1[key]
        elif key not in file1:
            if isinstance(file2[key], bool):
                value = str(file2[key]).lower()
            else:
                value = file2[key]

        if key not in file2:
            strings.append(f'  - {key}: {value}')
        elif key not in file1:
            strings.append(f'  + {key}: {value}')
        elif file1[key] == file2[key]:
            strings.append(f'    {key}: {value1}')
        else:
            strings.append(f'  - {key}: {value1}')
            strings.append(f'  + {key}: {value2}')
    strings.append('}')

    return '\n'.join(strings)


# 1. Сделать отступы слева
# 2. Сделать булевы значения .lower()
# 3. Проверить тестами
# 4. ci.yaml
