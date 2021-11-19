import requests
import sqlite3
import json

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

response = requests.get('https://rasp.omgtu.ru/api/search?term=в&type=person')
data = response.json()

cursor.executescript('''
CREATE TABLE if not exists teachers (id varchar(8000), description text, label text, type text)
''')

for teacher in data:
    cursor.execute("insert into teachers values (?, ?, ?, ?)",
                    [teacher['id'], teacher['description'], teacher['label'],teacher['type']])
    conn.commit()