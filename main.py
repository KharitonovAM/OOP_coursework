from src.utils_vacancies import Vacancies
from src.utils_api import HH
from src.utils_filework import FileWork
from src.oter_utils import DataWork


def main():
    '''Функция отвечающая за взаимодействие с пользователем'''

    other_functions = DataWork()

    while True:

        print('''
        \tДобро пожаловать в программу, которая позволит вам упростить взаимодействие с сайтом hh.ru для контроля вакансий
        Программа позволит вам упростить получение информации, и поддердивает следующий функционал: 
        - поиск по кючевому слову
        - фильтрацию по зарплате
        - возможность вывести ограниченное количество вакансий (с максимальной запрлатой)
        
        Данные по заработной плате валидируются, если значение не было указано, то оно принимает значение равное 0
         
        ''')

        work_control = input("\tЕсли хотите завершить работу программы нажмите Q\n")
        if work_control.upper() == 'Q':
            input('\nРабота программы прекращена. Хорошего дня!')
            break

        lookihg_word = input('Введите слово, по которому будем искать вакансии на сайте hh.ru\n')
        vacansy_object = HH()
        vacansy_list = vacansy_object.search_vacancion(lookihg_word)
        vacansy_object_list = list(map(other_functions.make_vacancy_object, vacansy_list))
        print(f'Поиск вакансий завершен, всго нашлось {len(vacansy_object_list)}')
        sorted_vacancy_list = other_functions.sort_vacancies(vacansy_object_list)
        for i, v in enumerate(vacansy_object_list):
            print(i,'---',v)
        sorted_vacancy_list = other_functions.sort_vacancies(vacansy_object_list)
        for i, v in enumerate(sorted_vacancy_list):
            print(i,'---',v.name, v.salary)
        input()



if __name__ == "__main__":
    main()