"""
Запуск тестов выполняется командой
python -m pytest 07_Pytest.py
"""

def test_upper():
    assert 'foo'.upper() == 'FOO'

def test_isupper():
    assert 'FOO'.isupper()

def test_failed_upper():
    assert 'foo'.upper() == 'Foo'