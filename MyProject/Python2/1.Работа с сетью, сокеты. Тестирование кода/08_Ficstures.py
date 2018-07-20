import pytest

def setup():
    print('01. setub Установка окружения по умолчанию в модуле')

def teardown():
    print('02. teardown Сброс окружения по умолчанию в модуле')

def setup_module(module):
    print('03. setup Установка окружения на уровне модуля')

def teardown_module(module):
    print('04. teardown Сброс окружения на уровне модуля')

def setup_function(function):
    print('05. setub Установка окружения на уровне функции')

def teardown_function(function):
    print('06. teardown Сброс окружения на уровне функции')

def test_number_3_4():
    print('07. >> test 3*4')
    assert 3*4 == 12

def test_strings_a_3():
    print('08. >> test a*3')
    assert 'a'*3 == 'aaa'

class TestUM:
    def setup(self):
        print('09. setub Установка окружения по умолчанию в классе')

    def teardown(self):
        print('10. teardown Сброс окружения по умолчанию в классе')

    @classmethod
    def setup_class(cls):
        print('11. setup Установка окружения на уровне класса')

    @classmethod
    def teardown_class(cls):
        print('12. teardown Сброс окружения на уровне класса')

    def setup_method(self, method):
        print('13. setup Установка на уровне метода')

    def teardown_method(self, method):
        print('14. teardown Сброс окружения на уровне метода')

    def test_number_5_6(self):
        print('15. >> test b*2')
        assert 'b'*2 == 'bb'