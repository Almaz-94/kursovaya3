import json
import datetime

with open('./operations.json',encoding='utf-8') as file:
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

def mask_card_info(info: str):
    '''
    Скрывает номера счетов и карт
    '''
    card_name=' '.join(info.split()[:-1])
    number=info.split().pop()
    if card_name=='Счет':
        tmp=''.join(['*' for _ in number[:-4]])
        number=tmp+number[-4:]
    else:
        number=''.join('*' if i in range(6,12) else num for i,num in enumerate(number))
        number=' '.join([number[i:i+4] for i in range(0,len(number),4)])
    return card_name+' '+number

def get_first_valid_operations(sorted_data):
    """
    Выводит на экран первые 5 операций
    """
    for i,elem in enumerate(sorted_data):
        date=elem['date'].strftime('%d.%m.%Y')
        try:
            from_=mask_card_info(elem['from'])
        except:
            from_ = ''
        to=mask_card_info(elem['to'])
        summa=elem['operationAmount']['amount']
        currency=elem['operationAmount']['currency']['name']

        print(f"{date} {elem['description']}\n"
              f"{from_} -> {to}\n"
              f"{summa} {currency}\n")

        if i==4:
            break


sorted_data=get_valid_operations(data)

get_first_valid_operations(sorted_data)