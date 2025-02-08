import logging
import json

from abc import ABC, abstractmethod
from setting.setting import DATA_FILENAME
from setting.log_setting import my_log_config


logging.basicConfig = my_log_config
# определяем именные логеры
logging_filename = logging.getLogger("utils_filework")
class AbsFileWork(ABC):

    @abstractmethod
    def take_data(self):
        pass

    @abstractmethod
    def write_data(self):
        pass


class FileWork(AbsFileWork):
    '''Класс по работе с файлами'''

    def __init__(self, filename = DATA_FILENAME):
        logging_filename.info("Старт инициализации")
        """Инициализация объекта который взаимодействует с файлами"""

        self.filename = filename
        logging_filename.info("Завершение инициализации")

    def write_data(self, data):
        '''метод который отвечает за внесение данных в json файл'''

        logging_filename.info(f"Пытаемся записать в {self.filename} данные")
        with open(self.filename, 'w') as f:
            json.dump(data, f)
        logging_filename.info(f"Данные в {self.filename} записаны")


    def take_data(self):
        '''Метод который отвечает за получение данных из json-файла
         и возвращает полченные значения'''

        logging_filename.info(f"Пытаемся прочитето из {self.filename} данные")
        with open(self.filename, 'r') as f:
            my_data = json.load(f)
        logging_filename.info(f"Данные из {self.filename} прочитаны")
        return my_data
