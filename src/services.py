import json
import datetime


def sum_cashback_by_category(transactions: list[dict], year: int, month: int) -> str:
    categories = {}
    for transaction in transactions:
        cashback = transaction['cash_back']
        if transaction["cash_back"] > 0:
            operation_date = transaction['operation_date']
            if operation_date.year == year and operation_date.month == month:
                category = transaction['category']

                if category in categories:
                    categories[category] += cashback
                else:
                    categories[category] = cashback
    return json.dumps(categories, ensure_ascii=False, indent=4)


print(sum_cashback_by_category(
    [{'operation_date': datetime.datetime(2018, 1, 14, 16, 5), 'card_num': '*7197', 'state': 'OK', 'sum_pay': -104.0,
      'cash_back': 50, 'category': 'Топливо', 'description': 'Neste'},
     {'operation_date': datetime.datetime(2018, 1, 14, 14, 10, 58), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -70.2,
      'cash_back': 0, 'category': 'Рестораны', 'description': 'Luhamaa Terminal  kohvik'},
     {'operation_date': datetime.datetime(2018, 1, 14, 10, 43, 42), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -99.68, 'cash_back': 200, 'category': 'Супермаркеты', 'description': 'Rimi Hm "Alfa"'},
     {'operation_date': datetime.datetime(2018, 1, 12, 16, 38, 58), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -324.32, 'cash_back': 0, 'category': 'Различные товары', 'description': 'Maxima Lv R010'},
     {'operation_date': datetime.datetime(2018, 1, 12, 16, 15, 56), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -1864.51, 'cash_back': 0, 'category': 'Одежда и обувь', 'description': 'Varaviksne-veikals'},
     {'operation_date': datetime.datetime(2018, 1, 12, 16, 4, 18), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -488.59, 'cash_back': 0, 'category': 'Одежда и обувь', 'description': 'Varaviksne-veikals'},
     {'operation_date': datetime.datetime(2018, 1, 12, 15, 58, 1), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -1985.96, 'cash_back': 300, 'category': 'Одежда и обувь', 'description': 'Varaviksne-veikals'},
     {'operation_date': datetime.datetime(2018, 1, 12, 11, 8, 52), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -1574.59, 'cash_back': 0, 'category': 'Супермаркеты', 'description': 'Rimi Hm Gramzdas'},
     {'operation_date': datetime.datetime(2018, 1, 11, 17, 21, 40), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -3089.97, 'cash_back': 0, 'category': 'Одежда и обувь', 'description': 'Veikals Rosme, Mukusalas'},
     {'operation_date': datetime.datetime(2018, 1, 11, 0, 0), 'card_num': '*7197', 'state': 'OK', 'sum_pay': -94.0,
      'cash_back': 0, 'category': 'Транспорт', 'description': 'Яндекс Такси'},
     {'operation_date': datetime.datetime(2018, 1, 10, 21, 31, 46), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -191.13, 'cash_back': 0, 'category': 'Топливо', 'description': 'Circle K'},
     {'operation_date': datetime.datetime(2018, 1, 10, 19, 10, 56), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -1041.74, 'cash_back': 0, 'category': 'Различные товары', 'description': 'DutyFree'},
     {'operation_date': datetime.datetime(2018, 1, 10, 16, 53, 21), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -634.0, 'cash_back': 100, 'category': 'Рестораны', 'description': 'Stedroll'},
     {'operation_date': datetime.datetime(2018, 1, 10, 14, 10, 2), 'card_num': None, 'state': 'OK', 'sum_pay': 25100.0,
      'cash_back': 0, 'category': 'Пополнения', 'description': 'Перевод с карты'},
     {'operation_date': datetime.datetime(2018, 1, 10, 13, 1, 22), 'card_num': None, 'state': 'OK', 'sum_pay': 27068.0,
      'cash_back': 0, 'category': 'Пополнения', 'description': 'Перевод с карты'},
     {'operation_date': datetime.datetime(2018, 1, 10, 13, 0, 4), 'card_num': None, 'state': 'OK', 'sum_pay': 30000.0,
      'cash_back': 0, 'category': 'Пополнения', 'description': 'Перевод с карты'},
     {'operation_date': datetime.datetime(2018, 1, 10, 12, 59, 23), 'card_num': None, 'state': 'OK', 'sum_pay': 30000.0,
      'cash_back': 0, 'category': 'Пополнения', 'description': 'Перевод с карты'},
     {'operation_date': datetime.datetime(2018, 1, 10, 12, 43, 34), 'card_num': '*5441', 'state': 'FAILED',
      'sum_pay': -30068.0, 'cash_back': 0, 'category': 'nan', 'description': 'Перевод с карты'},
     {'operation_date': datetime.datetime(2018, 1, 10, 12, 42, 44), 'card_num': '*5441', 'state': 'FAILED',
      'sum_pay': -40068.0, 'cash_back': 0, 'category': 'nan', 'description': 'Перевод с карты'},
     {'operation_date': datetime.datetime(2018, 1, 10, 12, 41, 24), 'card_num': '*5441', 'state': 'FAILED',
      'sum_pay': -87068.0, 'cash_back': 0, 'category': 'nan', 'description': 'Перевод с карты'},
     {'operation_date': datetime.datetime(2018, 1, 8, 21, 29, 43), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -364.49, 'cash_back': 0, 'category': 'Супермаркеты', 'description': 'Дикси'},
     {'operation_date': datetime.datetime(2018, 1, 8, 14, 21, 23), 'card_num': '*4556', 'state': 'OK',
      'sum_pay': -250.0,
      'cash_back': 0, 'category': 'Связь', 'description': 'МТС'},
     {'operation_date': datetime.datetime(2018, 1, 8, 13, 38, 8), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -1004.9,
      'cash_back': 0, 'category': 'Различные товары', 'description': 'Torgovyy Dom Mayak'},
     {'operation_date': datetime.datetime(2018, 1, 5, 15, 28, 22), 'card_num': '*7197', 'state': 'OK', 'sum_pay': -79.6,
      'cash_back': 34, 'category': 'Супермаркеты', 'description': 'Пятёрочка'},
     {'operation_date': datetime.datetime(2018, 1, 5, 14, 58, 38), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -120.0,
      'cash_back': 354, 'category': 'Цветы', 'description': 'Magazin  Prestizh'},
     {'operation_date': datetime.datetime(2018, 1, 4, 15, 0, 41), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -1025.0,
      'cash_back': 123, 'category': 'Топливо', 'description': 'Pskov AZS 12 K2'},
     {'operation_date': datetime.datetime(2018, 1, 4, 14, 5, 8), 'card_num': '*7197', 'state': 'OK', 'sum_pay': -1065.9,
      'cash_back': 16, 'category': 'Супермаркеты', 'description': 'Пятёрочка'},
     {'operation_date': datetime.datetime(2018, 1, 3, 15, 3, 35), 'card_num': '*7197', 'state': 'OK', 'sum_pay': -73.06,
      'cash_back': 20, 'category': 'Супермаркеты', 'description': 'Magazin 25'},
     {'operation_date': datetime.datetime(2018, 1, 3, 14, 55, 21), 'card_num': '*7197', 'state': 'OK', 'sum_pay': -21.0,
      'cash_back': 56, 'category': 'Красота', 'description': 'OOO Balid'},
     {'operation_date': datetime.datetime(2018, 1, 1, 20, 27, 51), 'card_num': '*7197', 'state': 'OK',
      'sum_pay': -316.0,
      'cash_back': 67, 'category': 'Красота', 'description': 'OOO Balid'},
     {'operation_date': datetime.datetime(2018, 1, 1, 12, 49, 53), 'card_num': None, 'state': 'OK', 'sum_pay': -3000.0,
      'cash_back': 45, 'category': 'Переводы', 'description': 'Линзомат ТЦ Юность'}],
    2018, 1))
