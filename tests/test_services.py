# from datetime import datetime
#
# import pytest
#
# from src.services import sum_cashback_by_category
#
#
# def test_sum_cashback_by_category():
#     assert sum_cashback_by_category([
#         {
#             "category": "Еда",
#             "cash_back": 100,
#             "operation_date": datetime(2024, 10, 5)
#         },
#         {
#             "category": "Одежда",
#             "cash_back": 50,
#             "operation_date": datetime(2024, 10, 15)
#         },
#         {
#             "category": "Развлечения",
#             "cash_back": 20,
#             "operation_date": datetime(2024, 10, 12)
#         },
#     ],
#         2024,
#         10
#     ) == {"Еда": 100, "Одежда": 50, "Развлечения": 20}
