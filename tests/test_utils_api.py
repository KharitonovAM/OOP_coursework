import pytest

from unittest.mock import patch, Mock

import src.utils_api
from src.utils_api import HH

@patch("requests.get")
def test_api_correct_work(get_mock, capsys):
    '''Мокирующий тест, который проверяет, что функция возвращает корректные данные'''

    get_mock.return_value = []
    z = src.utils_api.HH()
    assert z == []


@patch("requests.get")
def test_api_correct_work(get_mock, capsys):
    '''Мокирующий тест, который проверяет, что функция возвращает корректные данные'''

    get_mock.return_value = []
    z = src.utils_api.HH()
    z.search_vacancion('Медпроф')
    text_out = capsys.readouterr()
    assert text_out.out == 'Работа поиска завершена, всего найдено 0 вакансий\n'
