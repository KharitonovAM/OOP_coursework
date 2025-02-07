from abc import ABC, abstractmethod

class AbstractHH(ABC):

    '''Абстрактный класс который моделирует создание классов по работе с API сайта HH.ru'''

    @abstractmethod
    def __str__(self):
        pass


    @abstractmethod
    def take_looking_vakancy_name(self):
        pass


    @abstractmethod
    def search_vacancion(self):
        pass
