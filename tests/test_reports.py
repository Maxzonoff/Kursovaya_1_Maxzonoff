import datetime

import pandas as pd
import pytest

from src import reports


@pytest.fixture
def test_df():
    data = {
        "name": ["name_1", "name_2", "name_3", "name_4"],
        "category": ["category_1", "category_2", "category_1", "category_1"],
        "date": [
            datetime.date(2024, 10, 12),
            datetime.date(2024, 10, 12),
            datetime.date(2024, 7, 15),
            datetime.date(2024, 5, 12),
        ],
    }

    df = pd.DataFrame(data)

    return df


def test_spending_by_category(test_df):
    result = reports.spending_by_category(test_df, "category_1", "12.10.2024")
    pd.testing.assert_frame_equal(
        result,
        pd.DataFrame(
            {
                "name": ["name_1", "name_3"],
                "category": ["category_1", "category_1"],
                "date": [datetime.date(2024, 10, 12), datetime.date(2024, 7, 15)],
            }
        ),
    )
