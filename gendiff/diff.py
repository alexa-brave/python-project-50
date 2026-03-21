def generate_diff(file1, file2) -> str:

    keys = sorted(file1.keys() | file2.keys())
    strings = ['{']

    for key in keys:
        if key not in file2:
            strings.append(f'- {key}: {file1[key]}')
        elif key not in file1:
            strings.append(f'+ {key}: {file2[key]}')
        elif file1[key] == file2[key]:
            strings.append(f'  {key}: {file1[key]}')
        else:
            strings.append(f'- {key}: {file1[key]}')
            strings.append(f'+ {key}: {file2[key]}')
    strings.append('}')

    return '\n'.join(strings)
