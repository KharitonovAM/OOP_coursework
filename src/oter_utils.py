from src.utils_vacancies import Vacancies

class DataWork():
    '''вспомогательные функции предназначенные для упрощения работы прораммы'''

    def sort_vacancies(self, vac_list):
        '''Принимает на вход список объектов класса Vacancy и возвращает список отсортированные по верхнему пределу зарплаты'''

        sorted_list = sorted(vac_list, key = lambda x: x.salary['to'], reverse=True)

        return sorted_list


    def make_vacancy_object(self, vacation_data):
        '''Формирует объект класса вакансии из списка полученного чрез API'''
        return Vacancies(vacation_data['name'], vacation_data['address'], vacation_data['salary'], vacation_data['alternate_url'], vacation_data['work_schedule_by_days'])