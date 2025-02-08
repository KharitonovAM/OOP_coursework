import pytest
from src.utils_api import HH

@pytest.fixture
def medprof_test_result():
    return [{'id': '115181031', 'premium': False, 'name': 'Курьер пеший', 'department': None, 'has_test': False, 'response_letter_required': False,
             'area': {'id': '2', 'name': 'Санкт-Петербург', 'url': 'https://api.hh.ru/areas/2'}, 'salary': {'from': 49280, 'to': 60480, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Санкт-Петербург', 'street': 'Лиговский проспект', 'building': '94к2', 'lat': 59.920294, 'lng': 30.355556, 'description': None,
                         'raw': 'Санкт-Петербург, Лиговский проспект, 94к2', 'metro': None, 'metro_stations': [], 'id': '13319383'},
             'response_url': None, 'sort_point_distance': None, 'published_at': '2025-02-05T17:55:13+0300',
             'created_at': '2025-02-05T17:55:13+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=115181031', 'show_logo_in_search': None,
             'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/115181031?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/115181031', 'relations': [], 'employer':
                 {'id': '9754213', 'name': 'МедПроф', 'url': 'https://api.hh.ru/employers/9754213',
                  'alternate_url': 'https://hh.ru/employer/9754213', 'logo_urls':
                      {'original': 'https://img.hhcdn.ru/employer-logo-original/1260472.jpg',
                       '90': 'https://img.hhcdn.ru/employer-logo/6662214.jpeg', '240': 'https://img.hhcdn.ru/employer-logo/6662215.jpeg'},
                  'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9754213', 'accredited_it_employer': False, 'trusted': True},
             'snippet': {'requirement': 'Доброжелательность и желание развиваться вместе с нашей компанией. Ответственность. Пунктуальность. '
                                        'Мы готовы рассмотреть кандидатов без опыта работы.',
                         'responsibility': 'Обеспечение своевременной доставки медицинских документов из медицинских центров для Клиентов. '
                                           'Обеспечение безопасности и конфиденциальности документов. Обеспечение целостности документов.'},
             'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [],
             'working_time_modes': [], 'accept_temporary': True, 'fly_in_fly_out_duration': [], 'work_format': [], 'working_hours':
                 [{'id': 'HOURS_8', 'name': '8\xa0часов'}], 'work_schedule_by_days': [{'id': 'FIVE_ON_TWO_OFF', 'name': '5/2'}], 'night_shifts': False,
             'professional_roles': [{'id': '58', 'name': 'Курьер'}], 'accept_incomplete_resumes': True, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'employment_form': {'id': 'FULL', 'name': 'Полная'}, 'internship': False,
             'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}]