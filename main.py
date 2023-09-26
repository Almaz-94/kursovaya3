import json
import datetime

with open('operations.json',encoding='utf-8') as file:
    data=json.load(file)

def get_valid_operations(data):
    """
    Сортирует и отбирает выполненные операции
    """
    valid_data=[]
    for elem in data:
        if len(elem) == 0:
            continue
        if elem['state'] == 'EXECUTED':
            elem['date']=datetime.datetime.strptime(elem['date'], '%Y-%m-%dT%H:%M:%S.%f')
            valid_data.append(elem)
    return sorted(valid_data,key=lambda x: x['date'],reverse=True)

def get_first_valid_operations(data):
    """
    Выводит на экран первые 5 операций
    """
    for i,elem in enumerate(data):
        date=elem['date'].strftime('%d.%m.%Y')
        try:
            from_=elem['from']
        except:
            from_ = ''
        to=elem['to']
        summa=elem['operationAmount']['amount']
        currency=elem['operationAmount']['currency']['name']

        print(f"{date} {elem['description']}\n"
              f"{from_} -> {to}\n"
              f"{summa} {currency}\n")

        if i==4:
            break

sorted_data=get_valid_operations(data)

get_first_valid_operations(sorted_data)