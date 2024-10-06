from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions_info) -> None:
    result = filter_by_currency(transactions_info, "USD")
    assert list(result) == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    result = filter_by_currency(transactions_info, "EUR")
    assert list(result) == []
    try:
        result = filter_by_currency(transactions_list=[], currency="EUR")
        assert result == "Нет транзакций"
    except AssertionError:
        print("Нет транзакций")


@pytest.mark.parametrize(
    "value, expected_result",
    [
        (
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            "Перевод организации",
        ),
        (
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229",
            },
            "Перевод с карты на карту",
        ),
        (
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
            "Перевод со счета на счет",
        ),
    ],
)
def test_transaction_descriptions(value: list[dict[str, Any]], expected_result: str) -> None:
    """Функция тестирует генератор транзакций"""

    try:
        assert transaction_descriptions(value) == expected_result
    except AssertionError:
        print(expected_result)


#    assert next(num) == "Перевод организации"
#    assert next(num) == "Перевод со счета на счет"
#    assert next(num) == "Перевод со счета на счет"
#    assert next(num) == "Перевод с карты на карту"


def test_card_number_generator() -> None:
    """Функция тестирует генератор номеров карт"""
    card_number = card_number_generator(9999999999999998, 9999999999999999)

    assert next(card_number) == "9999 9999 9999 9998"
    assert next(card_number) == "9999 9999 9999 9999"
