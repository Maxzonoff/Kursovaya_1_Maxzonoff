import datetime


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
