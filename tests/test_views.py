from unittest.mock import patch
import json
from src import utils
from src import views
from src.views import main_page


def test_main_page():
    date = "2024-09-21 14:24:30"
    result = json.loads(views.main_page(date))
    assert result["greeting"] == "Добрый день"


@patch('src.utils.convert_to_datetime')
@patch('src.utils.greeting_by_time')
@patch('src.utils.read_excel')
@patch('src.utils.get_exchange_rates')
@patch('src.utils.get_stock_prices')
@patch('src.filters.month_filter')
@patch('src.utils.transactions_total_sum')
@patch('src.utils.top_transactions')
def test_main_page_ok(mock_top_transactions, mock_transactions_total, mock_month_filter,
                      mock_get_stock_prices, mock_get_exchange_rates, mock_read_excel,
                      mock_greeting_by_time, mock_convert_to_datetime):
    mock_convert_to_datetime.return_value = utils.convert_to_datetime("2021-12-28 13:29:30")
    mock_greeting_by_time.return_value = "Добрый день"
    mock_read_excel.return_value = [{"operation_date": "2021-12-28", "amount": 1000}]
    mock_month_filter.return_value = [{"operation_date": "2021-12-28", "amount": 1000}]
    mock_transactions_total.return_value = {"total_sum": 1000}
    mock_top_transactions.return_value = [{"operation_date": "2021-12-28", "amount": 1000}]
    mock_get_exchange_rates.return_value = {"USD": 74.0, "EUR": 85.0}
    mock_get_stock_prices.return_value = {"AAPL": 150.0, "GOOGL": 2800.0}

    result = main_page("2021-12-28 13:29:30")

    expected_result = {
        "greeting": "Добрый день",
        "cards": {"total_sum": 1000},
        "top_transactions": [{"operation_date": "2021-12-28", "amount": 1000}],
        "currency_rates": {"USD": 74.0, "EUR": 85.0},
        "stock_prices": {"AAPL": 150.0, "GOOGL": 2800.0}
    }

    assert json.loads(result) == expected_result


@patch('src.utils.convert_to_datetime')
def test_main_page_invalid_date(mock_convert_to_datetime):
    mock_convert_to_datetime.side_effect = ValueError("Invalid date format")

    result = main_page("invalid-date")

    expected_result = {"error": "Invalid date format"}

    assert json.loads(result) == expected_result


@patch('src.utils.read_excel')
def test_main_page_file_not_found(mock_read_excel):
    mock_read_excel.side_effect = FileNotFoundError("File not found")

    result = main_page("2021-12-28 13:29:30")

    expected_result = {"error": "Operations file not found"}

    assert json.loads(result) == expected_result
