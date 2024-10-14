import pandas as pd
import datetime
import logging

logger = logging.getLogger(__name__)

if not logger.hasHandlers():
    file_handler = logging.FileHandler('../logs/log_file.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)


def save_to_file(func):
    """Функция-декоратор сохраняет данные в JSON файл."""

    def wrapper(*args, **kwargs):
        df = func(*args, **kwargs)
        data_json = df.to_json(orient='records')
        with open('../data/reports.json', 'w') as f:
            f.write(data_json)
        logger.info("Данные сохранены в файл reports.json")

        return df

    return wrapper


@save_to_file
def spending_by_category(
        transactions: pd.DataFrame,
        category: str,
        date: str | None = None) -> pd.DataFrame:
    """Функция принимает DataFrame и возвращает JSON с тратами по категориям за три месяца."""

    if date is None:
        dt = datetime.date.today()
        logger.info(f"Дата не указана, использована текущая дата: {dt}")
    else:
        try:
            dt = datetime.datetime.strptime(date, '%d.%m.%Y').date()
            logger.info(f"Использована дата: {dt}")
        except ValueError as e:
            logger.error(f"Неверный формат даты: {date}. Ошибка: {e}")
            raise

    start_dt = dt - datetime.timedelta(days=90)
    logging.info(f"Период: с {start_dt} по {dt}")

    df = transactions.loc[transactions.category.isin([category])]
    df = df[(df['date'] >= start_dt) & (df['date'] <= dt)]

    logging.info(f"Найдено {len(df)} транзакций в категории '{category}' за указанный период")
    return df.reset_index(drop=True)
