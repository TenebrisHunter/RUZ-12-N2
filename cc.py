import requests
import json

names =  input()
names1= names.split()
aq=[]
for i in names1:
    a = requests.get('https://rasp.omgtu.ru/api/search?term='+str(i)+'&type=person')
    loadJSON = a.json()
    load = loadJSON[0]['id']
    start = "2021.11.11"
    response = requests.get('https://rasp.omgtu.ru/api/schedule/person/'+str(load), params={
                "start": start,
                "finish": start,
                "lng": 1
                })
    aboba = response.json()
    aq.append(aboba)
print(aq)