import requests
import re

count = 0
url = 'https://api.hh.ru/vacancies/'
# need_skills = ['SQL', 'Oracle']


par = {'text': '("Проблемно-ориентированный" OR "Проблемно ориентированный") '
               'OR (Администратор OR Administrator OR Аналитик or Analyst) '
               'AND (производительности OR "баз данных" OR бд OR "хранилища данных" OR Database OR DB) '
               'OR (АБД OR DBA OR СУБД OR "Система управления базами данных" OR "Database Management System" OR DBMS OR DMS)',
       'premium': 'false', 'area': 1261, 'per_page': '100', 'page': 2}
print('Порядок\tID Вакансии\tОбъявление\tГород\tКомпания\tКлючевые навыки')
for i in requests.get(url, params=par).json()['items']:
    vacancy_string = ''
    key_skills_string = '"'
    snippet_string = '"'

    vac_id = i['id']
    vac_name = i['name']

    vacancy = requests.get('https://api.hh.ru/vacancies/' + vac_id).json()
    key_skills = vacancy['key_skills']
    for e in key_skills:
        skill = e['name']
        if skill is not None:
            key_skills_string += skill + '\\&&\\'
    key_skills_string += '"'
    area = vacancy['area']
    employer = vacancy['employer']
    count += 1
    vacancy_string += str(count) + '\t' + vac_id + '\t' + vac_name + '\t' + area['name'] + '\t' + employer['name'] + '\t'
    print(vacancy_string + key_skills_string)
