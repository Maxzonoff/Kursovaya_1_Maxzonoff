import json

from src import views


def test_main_page():
    date = "2024-09-21 14:24:30"
    result = json.loads(views.main_page(date))
    assert result["greeting"] == "Добрый день"
