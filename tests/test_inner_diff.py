from gendiff.find_diff import build_diff


# тестируем внутренний diff
def test_build_diff_changed():
    first = {'a': 1}
    second = {'a': 2}

    expected = {
        'a': {
            'status': 'changed',
            'old_value': 1,
            'new_value': 2,
        }
    }

    assert build_diff(first, second) == expected


def test_build_diff_added_deleted_same():
    first = {'a': 1, 'b': 2}
    second = {'b': 2, 'c': 3}

    expected = {
        'a': {
            'status': 'deleted',
            'value': 1,
        },
        'b': {
            'status': 'same',
            'value': 2,
        },
        'c': {
            'status': 'added',
            'value': 3,
        },
    }

    assert build_diff(first, second) == expected


def test_build_diff_nested():
    first = {'common': {'key': 'value'}}
    second = {'common': {'key': 'value', 'ops': 'vops'}}

    expected = {
        'common': {
            'status': 'nested',
            'children': {
                'key': {
                    'status': 'same',
                    'value': 'value',
                },
                'ops': {
                    'status': 'added',
                    'value': 'vops',
                },
            },
        },
    }

    assert build_diff(first, second) == expected
