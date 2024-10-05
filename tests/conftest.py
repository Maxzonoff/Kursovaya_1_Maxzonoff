from datetime import datetime

import pytest


@pytest.fixture
def transaction():
    return [
        {
            "operation_date": datetime.datetime(2018, 1, 11, 0, 0),
            "card_num": "*7197",
            "state": "OK",
            "sum_pay": -94.0,
            "cash_back": 0,
            "category": "Транспорт",
            "description": "Яндекс Такси",
        },
        {
            "operation_date": datetime.datetime(2018, 1, 10, 21, 31, 46),
            "card_num": "*7197",
            "state": "OK",
            "sum_pay": -191.13,
            "cash_back": 0,
            "category": "Топливо",
            "description": "Circle K",
        },
        {
            "operation_date": datetime.datetime(2018, 1, 10, 19, 10, 56),
            "card_num": "*7197",
            "state": "OK",
            "sum_pay": -1041.74,
            "cash_back": 0,
            "category": "Различные товары",
            "description": "DutyFree",
        },
        {
            "operation_date": datetime.datetime(2018, 1, 10, 16, 53, 21),
            "card_num": "*7197",
            "state": "OK",
            "sum_pay": -634.0,
            "cash_back": 0,
            "category": "Рестораны",
            "description": "Stedroll",
        },
        {
            "operation_date": datetime.datetime(2018, 1, 10, 14, 10, 2),
            "card_num": None,
            "state": "OK",
            "sum_pay": 25100.0,
            "cash_back": 0,
            "category": "Пополнения",
            "description": "Перевод с карты",
        },
        {
            "operation_date": datetime.datetime(2018, 1, 10, 13, 1, 22),
            "card_num": None,
            "state": "OK",
            "sum_pay": 27068.0,
            "cash_back": 0,
            "category": "Пополнения",
            "description": "Перевод с карты",
        },
        {
            "operation_date": datetime.datetime(2018, 1, 10, 13, 0, 4),
            "card_num": None,
            "state": "OK",
            "sum_pay": 30000.0,
            "cash_back": 0,
            "category": "Пополнения",
            "description": "Перевод с карты",
        },
    ]
