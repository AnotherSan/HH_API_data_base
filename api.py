import requests
import re

count = 0
url = 'https://api.hh.ru/vacancies/'
# need_skills = ['SQL', 'Oracle']


par = {'text': '"Администратор баз данных" OR "Administrator Database" OR "Administrator DB"',
       'premium': 'false', 'area': 1, 'per_page': '10', 'page': -1}
print('Порядок\tID Вакансии\tОбъявление\tГород\tКомпания\tКлючевые навыки')
for i in requests.get(url, params=par).json()['items']:
    vacancy_string = ''
    key_skills_string = '"'
    lists_string = ''
    vac_id = i['id']
    vac_name = i['name']

    vacancy = requests.get('https://api.hh.ru/vacancies/' + vac_id).json()
    key_skills = vacancy['key_skills']
    # print(vacancy['description'])
    ul_list = re.findall(r'<ul>(.*?)</ul>', vacancy['description'], flags=re.IGNORECASE)
    for ul in ul_list:
        element_lists_string = '"'
        li_list = re.findall(r'<li>(.*?)</li>', ul)
        for li in li_list:
            li = re.sub(r'<.*?>', ' ', li)
            element_lists_string += li + '\\&&\\'
        lists_string += element_lists_string + '"' + '\t'

    for e in key_skills:
        skill = e['name']
        if skill is not None:
            key_skills_string += skill + '\\&&\\'
    key_skills_string += '"'
    area = vacancy['area']
    employer = vacancy['employer']
    count += 1
    vacancy_string += str(count) + '\t' + vac_id + '\t' + vac_name + '\t' + area['name'] + '\t' + employer['name'] \
                      + '\t' + key_skills_string + '\t' + lists_string
    print(vacancy_string)
