import requests
import logging
from abc import ABC, abstractmethod

from setting.log_setting import my_log_config


logging.basicConfig = my_log_config
# определяем именные логеры
logging_api = logging.getLogger("api_utils")
class AbstractHH(ABC):
    '''Абстрактный класс который моделирует создание классов по работе с API сайта HH.ru'''

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def search_vacancion(self):
        pass

class HH(AbstractHH):
    '''класс который взаимодействует с сайтом hh через API'''

    def __init__(self):
        '''Инициализация объекта класса HH'''


        logging_api.info('Старт инициализации объекта классса HH') #логирование
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        logging_api.info(f'Инициализации объекта классса HH завершена, параметры {self.params}') #логирование


    def search_vacancion(self, keyword):
        """Производит поиск на сайте hh.ru вакансий, которые содержат искомый текст"""

        logging_api.info(f'Старт сбора вакансий по тексту {keyword}')  # логирование
        self.params['text'] = keyword
        while True:
            try:
                logging_api.info(f'Обработали информацию по странице № {self.params['page']}')  # логирование
                response = requests.get(self.url, headers=self.headers, params=self.params)
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.params['page'] += 1
            except:
                print(f'Работа поиска завершена, всего найдено {len(self.vacancies)} вакансий')
                logging_api.info('Завершена обработка поиска вакансий')
                break

    def __str__(self):
        """Выыодит на печать нформацию ою объекте класса HH"""
        logging_api.info(f'Вызван на печать объект класса {self.__class__.__name__}, текущие парамметры: {self.params} содержит {len(self.vacancies)} вакансий')
        return f'Класс {self.__class__.__name__}, текущие парамметры: {self.params} содержит {len(self.vacancies)} вакансий'


if __name__ == '__main__':
    z = HH()
    print(z)
    z.search_vacancion('медпроф')
    print(z)
