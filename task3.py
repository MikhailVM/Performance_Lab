import json


def fill_json(text):
    if isinstance(text, dict):
        for item in text:
            if isinstance(text[item], list):
                for x in text[item]:
                    if x['id'] in new:
                       x['value'] = new[x['id']]
                    if x.get('values'):
                        fill_json(x['values'])
    elif isinstance(text, list):
        for y in text:
            if y['id'] in new:
                y['value'] = new[y['id']]
            if y.get('values'):
                fill_json(y['values'])


name_1 = input('Введите имя файла структуры: ')
name_2 = input('Введите имя файла с результатами теста: ')

with open(name_1, 'r') as file_1:
    report = json.load(file_1)

new = {}

with open(name_2, 'r') as file_2:
    data = json.load(file_2)
    for elem in data['values']:
        new[elem['id']] = elem['value']

fill_json(report)

with open('report.json', 'w') as outfile:
    json.dump(report, outfile)
