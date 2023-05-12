import requests
import sqlite3
import json

conn = sqlite3.connect('rasp/db.sqlite3')
cursor = conn.cursor()

cursor.executescript('''
CREATE TABLE if not exists teachers (id varchar(8000), description text, label text, type text)
''')

def check():
    data = response.json()
    for teacher in data:
        cursor.execute(f"SELECT label FROM teachers WHERE id = {teacher['id']} ")
        if cursor.fetchone() is None:
            cursor.execute(f"insert into teachers values (?, ?, ?, ?)",
                            [teacher['id'], teacher['description'], teacher['label'],teacher['type']])
            conn.commit()
        else:
            pass

dict = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

for i in dict:
    response = requests.get('https://rasp.omgtu.ru/api/search?term='+i+'&type=person')
    check()
    for o in dict:
        response = requests.get('https://rasp.omgtu.ru/api/search?term='+i+o+'&type=person')
        check()
        for p in dict:
            response = requests.get('https://rasp.omgtu.ru/api/search?term='+i+o+p+'&type=person')
            check()