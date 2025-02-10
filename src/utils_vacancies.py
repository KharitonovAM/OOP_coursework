import logging
from abc import ABC, abstractmethod
from setting.log_setting import my_log_config


logging.basicConfig = my_log_config
vacancy_log = logging.getLogger('vacancy_modul_log')
class abstract_vacancies(ABC):
    '''Абстрактный класс для работы с вакансииями'''

    @abstractmethod
    def vacancy_data(self):
        pass


    @abstractmethod
    def __str__(self):
        pass


    @abstractmethod
    def validation_solary_vacancy_from(self):
        pass


    @abstractmethod
    def validation_solary_vacancy_to(self):
        pass


    @abstractmethod
    def compare_jobs(self):
        pass


class Vacancies:
    '''Класс для работы с объектами вакансий'''
    vacancies_object_list = []

    def __init__(self, name, address, salary, vacancies_url, work_format):
        """Инициализация объекта класса Vacancies"""

        vacancy_log.info(f'Старт инициализации объекта класса Vacancies c входными данными {name}, {address}, {salary}, {vacancies_url}, {work_format}')
        self.name = name
        self.address = address
        self.salary = salary
        self.validation_solary_vacancy_from()
        self.validation_solary_vacancy_to()
        self.vacancies_url = vacancies_url
        self.work_format = work_format
        vacancy_log.info('Завершена инициализация объекта класса Vacancies')

    def __str__(self):
        '''метод который определяет результат функции print для объекта классса Vacancies'''
        return f'Объект класса Vacancies {self.name}, {self.address}, {self.salary}, {self.vacancies_url}, {self.work_format} '

    def validation_solary_vacancy_from(self):
        '''Валидирует значение зарплаты указанное в ваканссии по нижнему критерию.
        если данных нет, или они не относится к ччиловому формату - ставит 0,
        если данные ниже нуля, так же заменяет на 0 значение'''

        vacancy_log.info(f'Старт валидации запрлаты по нижнему значение, на входе равно {self.salary['from']}')
        if isinstance(self.salary['from'], (float, int)) is False or self.salary['from'] < 0:
            self.salary['from'] = 0
        vacancy_log.info(f'Валидация запрлаты по нижнему значению проведена, по выходу {self.salary['from']}')

    def validation_solary_vacancy_to(self):
        '''Валидирует значение зарплаты по вверхнему пределу
        если значения нет, оно не ччисловое или меньше нижнего предела
        - возвращает значение нижнего предела'''

        vacancy_log.info(f'Старт валидации запрлаты по верхнему значению, на входе равно {self.salary['to']}')
        if isinstance(self.salary['to'], (float, int)) is False or self.salary['to'] < self.salary['from']:
            self.salary['to'] = self.salary['from']
        vacancy_log.info(f'Валидация запрлаты по верхнему значению проведена, по выходу {self.salary['to']}')


    def check_object_class(self, test_object):
        """Проверяет принадлежность объекта к классу Вакансии и возбуждает исключение если объект не соответствует классу"""

        try:
            isinstance(test_object, self.__class__.__name__)
        except Exception as e:
            print('Выбран объект не подходящего классса')


    def compare_jobs(self, vac2):
        '''Принимает две объекта класса вакансии и возвращает ту. у которой более высокая максмальная зарплата'''

        self.check_object_class(vac2)
        if max(self.salary['to'], vac2.salary['to']) == self.salary['to'] : return self
        elif max(self.salary['to'], vac2.salary['to']) == vac2.salary['to'] : return vac2
        elif max(self.salary['from'], vac2.salary['from']) == vac2.salary['from'] : return vac2
        elif max(self.salary['from'], vac2.salary['from']) == self.salary['from'] : return self
        print('Обе вакансии равнознчные по зарплатным условиям, поэтому оставили как есть')
        return self
