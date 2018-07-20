"""
python -m pytest -v -s 10_FixturesParam.py
"""
import pytest


def strange_string_func(s):
    """
    Подопытная функция для тестов
    """
    if len(s) > 5:
        return s + '?'
    elif len(s) < 5:
        return s + '!'
    else:
        return s + '.'


@pytest.fixture(scope='function', params=[
    ("abcdefg", "abcdefg?"),
    ("abc", "abc!"),
    ("abcde", "abcde.")
])
def param_test(request):
    return request.param


def test_strange_string_func(param_test):
    in_str, expected_output = param_test
    result = strange_string_func(in_str)
    print('\ninput: {0}, output: {1}, extended: {2}'.format(in_str, result, expected_output))
    assert result == expected_output
