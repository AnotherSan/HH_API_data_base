import requests
x=[]
count=0
result=[]
key=[]
url = 'https://api.hh.ru/vacancies/'
par = {'text': 'администратор баз данных','premium':'true','area':1261,'per_page':'100', 'page':[el for el in range(0,20)]}#1261
r = requests.get(url, params=par)
e=r.json()
#x.append(e)
y = e['items']
for i in y:
    if i['name']!=None:
        vacancies=i['name']
    if i['id']!=None:
        ide=i['id']
        vac='https://api.hh.ru/vacancies/'+ide
        req=requests.get(vac)
        eid=req.json()
        if eid['area']!=None:
            area=eid['area']
            if area['name']!=None:
                city=area['name']
                town=str(city)
        if eid['employer']!=None:
            employer=eid['employer']
            if employer['name']!=None:
                emName=employer['name']
                em=str(emName)
        if eid['key_skills']!=None:
            ks=eid['key_skills']
            key_name_list=[]
            for el in ks:
                if el['name']!=None:
                    name=el['name']
                    key_name_list.append(str(name))
        count=count+1
        co=str(count)
        words=co+town+' '+em
        print(vacancies,ide,words,[item for item in key_name_list])























