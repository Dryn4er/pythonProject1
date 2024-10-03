from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "value, expected_result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_filter_by_state(value: list[dict[str, Any]], expected_result: list[dict[str, Any]]) -> None:
    """Тест работоспособности через параметризацию"""
    assert filter_by_state(value) == expected_result


def state_filter_test(check_state: list[dict[str, Any]]) -> None:
    """Тест работоспособности базовый и с неизвестным значением"""
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == check_state
    )
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": None, "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": None, "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": None, "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": None, "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == []
    )


def test_sort_by_date(
    date_filtered: list[dict[str, Any]], same_date: list[dict[str, Any]], incorrect_date_format: list[dict[str, Any]]
) -> None:
    """Тест сортировки даты"""

    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == date_filtered
    )
    assert (
        sort_by_date(
            [
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2018-09-12T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
            ]
        )
        == same_date
    )
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "03072019T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == incorrect_date_format
    )
