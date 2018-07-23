"""
python -m pytest -s 09_FixturesExtended.py
"""
import pytest


@pytest.fixture()
def resource_setup(request):
    print('Подготовка ресурсов')

    def resource_teardown():  # Функция сброса окружения
        print('Освобождение ресурсов')

    request.addfinalizer(resource_teardown)  # Добавление финализатора


def test_1_that_needs_resource(resource_setup):
    print('test_1 - требуются ресурсы')


def test_2_that_does_not():
    print('test_2 - не требуются ресурсы')


def test_3_that_does_again(resource_setup):
    print('test_3 - требуются ресурсы')
