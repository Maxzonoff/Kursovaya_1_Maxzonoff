from src import filters, utils


def main_page(date: str) -> dict[str, str | list[dict]]:
    """
    Функция возвращает данные для главной страницы в формате:
    словаря с ключами:
    1. greeting - строка с приветствием в зависимости от времени
    2. cards - информация по каждой карте
    3. top_transactions - Топ-5 транзакций по сумме платежа.
    4. currency_rates - курсы валют
    5. stock_prices - Стоимость акций из S&P500.
    """

    dt = utils.convert_to_datetime(date)
    greeting = utils.greeting_by_time(dt.time())

    transactions = utils.read_excel("../data/operations.xlsx")
    monthly_transactions = filters.month_filter(transactions, dt.date(), key="operation_date")
    transactions_total = utils.transactions_total_sum(monthly_transactions)

    top_transactions = utils.top_transactions(monthly_transactions)

    result = {
        "greeting": greeting,
        "cards": transactions_total,
        "top_transactions": top_transactions,
    }
    # return json.dumps(result, indent=4, encoding="utf-8")
    return result


print(main_page("2021-12-28 13:29:30"))
print(main_page("2021-12-31 13:29:30"))
