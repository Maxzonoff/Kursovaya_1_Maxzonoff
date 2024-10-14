import json
import logging

from src import filters, utils

logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    file_handler = logging.FileHandler('../logs/log_file.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)
    logging.getLogger().setLevel(logging.INFO)

    logger.info('Запуск программы')


def main_page(date: str) -> str:
    """
    Функция возвращает данные для главной страницы в формате:
    словаря с ключами:
    1. greeting - строка с приветствием в зависимости от времени
    2. cards - информация по каждой карте
    3. top_transactions - Топ-5 транзакций по сумме платежа.
    4. currency_rates - курсы валют
    5. stock_prices - Стоимость акций из S&P500.
    """

    try:
        dt = utils.convert_to_datetime(date)
        logging.info(f"Дата успешно преобразована: {dt}")
    except ValueError as e:
        logging.error(f"Ошибка при преобразовании даты: {e}")
        return json.dumps({"error": "Invalid date format"})

    greeting = utils.greeting_by_time(dt.time())
    logger.info(f"Приветствие определено: {greeting}")

    try:
        transactions = utils.read_excel("../data/operations.xlsx")
        logger.info(f"Транзакции успешно загружены. Всего транзакций: {len(transactions)}")
    except FileNotFoundError as e:
        logger.error(f"Файл операций не найден: {e}")
        return json.dumps({"error": "Operations file not found"})
    except Exception as e:
        logger.error(f"Ошибка при загрузке транзакций: {e}")
        return json.dumps({"error": "Error loading transactions"})

    monthly_transactions = filters.month_filter(transactions, dt.date(), key="operation_date")
    transactions_total = utils.transactions_total_sum(monthly_transactions)
    logger.info(f"Подсчитана общая сумма транзакций по картам")

    top_transactions = utils.top_transactions(monthly_transactions)
    logger.info(f"Топ-5 транзакций получены")

    try:
        currency_rates = utils.get_exchange_rates()
        logger.info(f"Курсы валют успешно получены: {currency_rates}")
    except Exception as e:
        logger.error(f"Ошибка при получении курсов валют: {e}")
        currency_rates = []

    try:
        stock_prices = utils.get_stock_prices()
        logger.info(f"Цены на акции успешно получены: {stock_prices}")
    except Exception as e:
        logger.error(f"Ошибка при получении цен на акции: {e}")
        stock_prices = []

    result = {
        "greeting": greeting,
        "cards": transactions_total,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }

    logger.info("Данные для главной страницы успешно сформированы")
    return json.dumps(result, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print(main_page("2021-12-28 13:29:30"))
    print(main_page("2021-12-31 13:29:30"))
