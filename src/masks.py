from typing_extensions import Union

card_number = input()
account_number = input()


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция, которая маскирует номер карты"""

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция, которая маскирует номер счета"""

    return f"**{account_number[-4:]}"


print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
