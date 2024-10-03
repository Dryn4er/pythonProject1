from typing_extensions import Union


def get_mask_card_number(card_info: str) -> str:
    """Функция, которая маскирует номер карты"""

    if card_info.isdigit() and len(card_info) == 16:
        return f"{card_info[0:4]} {card_info[4:6]}** **** {card_info[12:16]}"
    elif card_info.isdigit() and len(card_info) != 16 and len(card_info) != 20:
        raise Exception("Введите корректный номер карты/счета")
    elif card_info.isdigit() and len(card_info) == 20:
        return f"**{card_info[-4:]}"
    elif card_info is None:
        return "Введите номер карты/счета"

    if not card_info.isdigit():
        numbers = []
        for i in card_info:
            if i.isdigit():
                numbers.append(i)
            else:
                continue
        if len(numbers) == 16:
            return f"{card_info[:-12]} {card_info[-12:-10]}** **** {card_info[-4:]}"


#        else:
#            raise Exception("Введите корректный номер карты/счета")


def get_mask_account(card_info: Union[int, str]) -> str:
    """Функция, которая маскирует номер счета"""

    return f"{card_info[0:5]}**{card_info[-4:]}"


# print(get_mask_card_number(card_info))
# print(get_mask_account(card_info))
