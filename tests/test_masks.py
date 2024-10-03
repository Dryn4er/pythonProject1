from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number(card_number: str, card_info: str) -> None:
    assert get_mask_card_number("7000792289606361") == card_number
    assert get_mask_card_number("Visa Platinum 7000792289606361") == card_info


#    with pytest.raises(Exception) as exc_info:
#        get_mask_card_number(card_info)
#    assert str(exc_info.value) == "Введите корректный номер карты/счета"


def test_mask_account(account_info: str, account_number: str) -> None:
    assert get_mask_account("Счет 73654108430135874305") == account_info
    assert get_mask_card_number("73654108430135874305") == account_number
