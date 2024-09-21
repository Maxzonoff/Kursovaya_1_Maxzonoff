from src import utils


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
    return {"greeting": greeting}
