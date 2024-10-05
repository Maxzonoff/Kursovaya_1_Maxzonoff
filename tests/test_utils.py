import datetime

import pytest

from src import utils
from src.utils import read_excel, transactions_total_sum


def test_convert_to_datetime():
    date = "2024-09-21 13:29:30"
    expected = datetime.datetime(
        year=2024,
        month=9,
        day=21,
        hour=13,
        minute=29,
        second=30,
    )
    assert utils.convert_to_datetime(date) == expected


def test_convert_to_datetime_invalid():
    invalid_date = "21-09-2024 13:29:30"
    with pytest.raises(ValueError):
        utils.convert_to_datetime(invalid_date)


@pytest.mark.parametrize(
    "time",
    [
        datetime.time(hour=6, minute=0, second=0),
        datetime.time(hour=11, minute=59, second=59),
        datetime.time(hour=8, minute=0, second=0),
    ],
)
def test_greeting_by_time_morning(time):
    expected = "Доброе утро"

    result = utils.greeting_by_time(time)

    assert result == expected


@pytest.mark.parametrize(
    "time",
    [
        datetime.time(hour=12, minute=0, second=0),
        datetime.time(hour=16, minute=59, second=59),
        datetime.time(hour=15, minute=0, second=0),
    ],
)
def test_greeting_by_time_day(time):
    expected = "Добрый день"

    result = utils.greeting_by_time(time)

    assert result == expected


@pytest.mark.parametrize(
    "time",
    [
        datetime.time(hour=17, minute=0, second=0),
        datetime.time(hour=20, minute=59, second=59),
        datetime.time(hour=19, minute=0, second=0),
    ],
)
def test_greeting_by_time_evening(time):
    expected = "Добрый вечер"

    result = utils.greeting_by_time(time)

    assert result == expected


@pytest.mark.parametrize(
    "time",
    [
        datetime.time(hour=21, minute=0, second=0),
        datetime.time(hour=1, minute=0, second=0),
        datetime.time(hour=5, minute=59, second=59),
    ],
)
def test_greeting_by_time_night(time):
    expected = "Доброй ночи"

    result = utils.greeting_by_time(time)

    assert result == expected


def test_transactions_total_sum():
    result = [
        {"last_digits": "*7197", "total_spent": -428, "cashback": 0},
        {"last_digits": "*5091", "total_spent": -564, "cashback": 0},
        {"last_digits": "*4556", "total_spent": 177635, "cashback": 70.0},
    ]
    assert transactions_total_sum(read_excel("test_files/test_data.xlsx")) == result


def test_transactions_total_sum_bad_path():
    with pytest.raises(FileNotFoundError) as f:
        transactions_total_sum(read_excel("test"))
        assert str(f.value) == "FileNotFoundError"


def test_read_excel_empty():
    assert read_excel("test_files/empty.xlsx") == []


def test_read_excel_good():
    assert read_excel("test_files/good.xlsx") == [
        {
            "operation_date": datetime.datetime(2021, 12, 31, 16, 44),
            "card_num": "*7197",
            "state": "OK",
            "sum_pay": -160.89,
            "cash_back": 0,
            "category": "Супермаркеты",
            "description": "Колхоз",
        }
    ]


def test_read_is_not_excel():
    with pytest.raises(ValueError):
        transactions_total_sum(read_excel("test_files/operations.json"))


# def test_read_excel(transaction):
#     result =
