import pytest

from main import get_valid_operations, get_first_valid_operations,mask_card_info
import json

@pytest.fixture
def get_data():
    with open('./operations.json', encoding='utf-8') as file:
        return json.load(file)

def test_get_valid_operations(get_data):
    sorted_data=get_valid_operations(get_data)
    for elem in sorted_data:
        assert len(elem)!=0
        assert elem['state'] == 'EXECUTED'

def test_mask_card_info():
    assert mask_card_info("Maestro 1596837868705199")=='Maestro 1596 83** **** 5199'
    assert mask_card_info("Счет 35383033474447895560")=='Счет ****************5560'
    assert mask_card_info("Visa Platinum 8990922113665229")=='Visa Platinum 8990 92** **** 5229'

def test_get_first_valid_operations(capfd,get_data):
    sorted_data = get_valid_operations(get_data)
    get_first_valid_operations(sorted_data)
    out,err=capfd.readouterr()
    assert out==\
'''08.12.2019 Открытие вклада
 -> Счет ****************5907
41096.24 USD

07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет ****************3655
48150.39 USD

19.11.2019 Перевод организации
Maestro 7810 84** **** 5568 -> Счет ****************2869
30153.72 руб.

13.11.2019 Перевод со счета на счет
Счет ****************9794 -> Счет ****************8125
62814.53 руб.

05.11.2019 Открытие вклада
 -> Счет ****************8381
21344.35 руб.\n\n'''

