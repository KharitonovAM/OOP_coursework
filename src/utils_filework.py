import logging
import json

from abc import ABC, abstractmethod
from setting.setting import FILENAME

class AbsFileWork(ABC):

    @abstractmethod
    def take_data(self):
        pass

    @abstractmethod
    def write_data(self):
        pass


class FileWork(abstractmethod):
    '''Класс по работе с файлами'''

    def __init__(self, filename = FILENAME):
        """Инициализация объекта который взаимодействует с файлами"""

        self.filename = filename

    def write_data(self, data):
        '''метод который отвечает за внесение данных в json файл'''

        with open(self.filename, 'a') as f:
            json.dump(data, f)


    def read_data(self):
        '''Метод который отвечает за получение данных из json-файла
         и возвращает полченные значения'''

        with open(self.filename, 'r') as f:
            my_data = json.load(f)
        return my_data
