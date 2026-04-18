from gendiff.formatters.value_format import format_value


def test_format_value_special():
    assert format_value(True, 1) == 'true'
    assert format_value(False, 1) == 'false'
    assert format_value(None, 1) == 'null'


def test_format_value_dict():
    value = {'a': 1}
    result = format_value(value, 1)

    assert result == (
        '{\n'
        '    a: 1\n'
        '}'
    )