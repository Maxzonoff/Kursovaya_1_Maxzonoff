import json


def sum_cashback_by_category(transactions: list[dict], year: int, month: int) -> str:
    """Функция возвращает сумму кэшбэка по каждой категории за выбранный период."""
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

    # print(sum_cashback_by_category([
    #     {
    #         "category": "Еда",
    #         "cash_back": 100,
    #         "operation_date": datetime(2024, 10, 5)
    #     },
    #     {
    #         "category": "Одежда",
    #         "cash_back": 50,
    #         "operation_date": datetime(2024, 10, 15)
    #     },
    #     {
    #         "category": "Развлечения",
    #         "cash_back": 20,
    #         "operation_date": datetime(2024, 10, 12)
    #     },
    # ],
    #     2024,
    10

# ))
