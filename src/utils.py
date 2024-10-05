import datetime
import json
import os
from math import isnan
import requests
from dotenv import load_dotenv
import pandas as pd


def convert_to_datetime(date: str) -> datetime.datetime:
    """
    :param date: строка в формате - 'YYYY-MM-DD HH:MM:SS'
    :return: datetime объект
    """
    dt_template = "%Y-%m-%d %H:%M:%S"
    dt = datetime.datetime.strptime(date, dt_template)
    return dt


def greeting_by_time(time: datetime.time) -> str:
    """Функция возвращает приветствие в зависимости от времени."""
    if 6 <= time.hour < 12:
        return "Доброе утро"
    if 12 <= time.hour < 17:
        return "Добрый день"
    if 17 <= time.hour < 21:
        return "Добрый вечер"
    return "Доброй ночи"


def read_excel(file_path: str) -> list[dict]:
    """Функция читает excel и возвращает
    список словарей со значениями во float"""
    data_file = pd.read_excel(file_path).to_dict("records")
    transactions = []
    for raw_transaction in data_file:
        operation_date = datetime.datetime.strptime(
            raw_transaction["Дата операции"],
            "%d.%m.%Y %H:%M:%S",
        )

        card_num = str(raw_transaction["Номер карты"])
        cash_back = float(raw_transaction["Кэшбэк"])
        if not isnan(cash_back):
            cash_back = float(cash_back)
        else:
            cash_back = 0
        if card_num == "nan":
            card_num = None
        transactions.append(
            {
                "operation_date": operation_date,
                "card_num": card_num,
                "state": raw_transaction["Статус"],
                "sum_pay": float(raw_transaction["Сумма платежа"]),
                "cash_back": cash_back,
                "category": str(raw_transaction["Категория"]),
                "description": str(raw_transaction["Описание"]),
            }
        )
    return transactions


def transactions_total_sum(transactions: list[dict]) -> list[dict]:
    total = {}
    for transaction in transactions:
        card_id = transaction["card_num"]
        if not card_id:
            continue

        if card_id not in total:
            total[card_id] = {"sum_pay": 0, "cash_back": 0}
        total[card_id]["sum_pay"] += round(transaction["sum_pay"])
        total[card_id]["cash_back"] += transaction["cash_back"]
    total_list = []
    for card_id, value in total.items():
        total_list.append(
            {
                "last_digits": card_id,
                "total_spent": value["sum_pay"],
                "cashback": value["cash_back"],
            }
        )

    return total_list


def top_transactions(transactions: list[dict]) -> list[dict]:
    sorted_transactions = sorted(transactions, key=lambda x: x["sum_pay"])
    result = sorted_transactions[:5]
    top_trans = []
    for elem in result:
        top_trans.append(
            {
                "date": elem["operation_date"].strftime("%d.%m.%Y"),
                "amount": elem["sum_pay"],
                "category": elem["category"],
                "description": elem["description"],
            }
        )
    return top_trans


def get_user_settings():
    with open('../user_settings.json') as f:
        return json.load(f)


def get_exchange_rates():
    load_dotenv()
    api_key = os.getenv('APILAYER_API_KEY')
    url = "https://api.apilayer.com/exchangerates_data/latest"

    user_settings = get_user_settings()

    currencies = ",".join(user_settings['user_currencies'])
    headers = {'apikey': api_key}
    params = {'base': 'RUB', 'symbols': currencies}
    response = requests.get(url, params, headers=headers, timeout=5)

    response.raise_for_status()
    content = response.json()
    currency_rates = []
    for cur, rate in content['rates'].items():
        currency_rates.append(
            {
                'currency': cur,
                'rate': 1 / rate,
            }
        )
    return currency_rates


def get_stock_prices():
    url = 'https://financialmodelingprep.com/api/v3/stock/list'
    load_dotenv()
    params = {'apikey': os.getenv('FMP_API_KEY')}
    response = requests.get(url, params)

    response.raise_for_status()
    content = response.json()
    stock_prices = []
    user_settings = get_user_settings()
    for stock in content:
        if stock['symbol'] in user_settings['user_stocks']:
            stock_prices.append(
                {
                    'stock': stock['symbol'],
                    'price': stock['price'],
                }
            )
    return stock_prices
