import pytest


@pytest.fixture()
def recource_setup(request):
    print('Подготовка ресурсов')

    def resource_teardown():  # Функция сброса окружения
        print('Освобождение ресурсов')

    request.addfinalizer(resource_teardown())  # Добавление финализатора


def test_1_that_needs_resource(recource_setup):
    print('test_1 - требуются ресурсы')


def test_2_that_does_not():
    print('test_2 - не требуются ресурсы')


def test_3_that_does_again(resource_setup):
    print('test_3 - требуются ресурсы')
