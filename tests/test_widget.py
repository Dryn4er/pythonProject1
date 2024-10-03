import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card: str, expected_result: str) -> None:
    assert mask_account_card(card) == expected_result


def test_get_date(check_date: str) -> None:
    assert get_date("2024-03-11T02:26:18.671407") == check_date
