import pytest

from Task1 import list_visit_russia
from Task2 import unique_id
from Task3 import chanel_max_volume
from api_yandeks import new_folder

@pytest.mark.parametrize('func, expected', [(list_visit_russia(), [{'visit1': ['Москва', 'Россия']},
                                                                 {'visit3': ['Владимир', 'Россия']},
                                                                 {'visit7': ['Тула', 'Россия']},
                                                                 {'visit8': ['Тула', 'Россия']},
                                                                 {'visit9': ['Курск', 'Россия']},
                                                                 {'visit10': ['Архангельск', 'Россия']}])])
def test_task1(func, expected):
    assert func == expected

@pytest.mark.parametrize('func, expected', [(unique_id(), [98, 35, 213, 54, 119, 15])])
def test_task2(func, expected):
    assert func == expected

@pytest.mark.parametrize('func, expected', [(chanel_max_volume(), 'yandex')])
def test_task3(func, expected):
    assert func == expected


@pytest.mark.parametrize('func, expected', [(new_folder.create_folder(), 201)])
def test_create_folder_1(func, expected):
    assert func == expected

@pytest.mark.parametrize('func, expected', [(new_folder.create_folder(), 409)])
def test_exist_folder(func, expected):
    assert func == expected

@pytest.mark.parametrize('func, expected', [(new_folder.get_folder(), 200)])
def test_create_folder_2(func, expected):
    assert func == expected

# new_folder.delete_folder()

@pytest.mark.parametrize('func, expected', [(new_folder.get_folder(), 404)])
def test_fault_create_folder(func, expected):
    assert func == expected