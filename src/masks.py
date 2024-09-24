from typing_extensions import Union


def get_mask_card_number(card_info: Union[int, str]) -> str:
    """Функция, которая маскирует номер карты"""

    return f"{card_info[:-12]} {card_info[-12:-10]}** ****{card_info[-4:]}"


def get_mask_account(card_info: Union[int, str]) -> str:
    """Функция, которая маскирует номер счета"""

    return f"{card_info[0:5]}**{card_info[-4:]}"


#print(get_mask_card_number(card_info))
#print(get_mask_account(card_info))

