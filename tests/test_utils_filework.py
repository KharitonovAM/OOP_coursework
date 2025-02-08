import pytest
import json
import os

from src.utils_filework import FileWork

def test_take_data(json_data_1):
    '''Тест который принимает на вход текстуру и проверяет,
    что в файл запиисываются данные совпадающие с текстурой'''

    temp_file = 'mydata.json'
    with open(temp_file, 'w') as mf:
        json.dump(json_data_1, mf)
    z = FileWork(temp_file)
    my_data = z.take_data()
    os.remove(temp_file)
    assert my_data == json_data_1


def test_write_data(json_data_1):
    """Тестирует, что функция по записи данных в json файл работает коректно"""

    temp_file = 'mydata.json'
    z = FileWork(temp_file)
    z.write_data(json_data_1)
    with open(temp_file, 'r') as mf:
        my_data = json.load(mf)
    os.remove(temp_file)
    assert my_data == json_data_1