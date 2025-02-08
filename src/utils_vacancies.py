import logging
import json
from abc import ABC, abstractmethod
from setting.log_setting import my_log_config
from setting.setting import LOG_FILE

class abstract_vacancies(ABC):

    @abstractmethod
    def vacancy_data(self):
        pass

    @abstractmethod
    def validation_vacancy(self):
        pass

    @abstractmethod
    def compare_jobs(self):
        pass

    def chooze_vacantion(self):
        pass
