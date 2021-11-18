import requests
 
f = open('aboba.txt', 'w')
dict = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
 
for i in dict:
    response = requests.get('https://rasp.omgtu.ru/api/search?term='+i+'&type=person')
    f.write(response.text)
    for o in dict:
        response = requests.get('https://rasp.omgtu.ru/api/search?term='+i+o+'&type=person')
        f.write(response.text)
        for p in dict:
            response = requests.get('https://rasp.omgtu.ru/api/search?term='+i+o+p+'&type=person')
            f.write(response.text)
f.close()