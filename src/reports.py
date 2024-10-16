import pandas as pd
import datetime


def save_to_file(func):
    """Функция-декоратор сохраняет данные в JSON файл."""

    def wrapper(*args, **kwargs):
        df = func(*args, **kwargs)
        data_json = df.to_json(orient='records')
        with open('../data/reports.json', 'w') as f:
            f.write(data_json)

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
    else:
        dt = datetime.datetime.strptime(date, '%d.%m.%Y').date()

    start_dt = dt - datetime.timedelta(days=90)

    df = transactions.loc[transactions.category.isin([category])]
    df = df[(df['date'] >= start_dt) & (df['date'] <= dt)]

    return df.reset_index(drop=True)
