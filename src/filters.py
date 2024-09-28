import datetime


def month_filter(lst: list[dict], date: datetime.date, key: str) -> list[dict]:
    """Функция фильтрует список lst по ключу key оставляя элементы
    по месяцу date и не больше date."""
    result = []
    for elem in lst:
        dt = elem[key]
        if dt.year != date.year or dt.month != date.month:
            continue
        if dt.day > date.day:
            continue
        result.append(elem)

    return result
