from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

#card_info = input()


# noinspection PyTypeChecker
def mask_account_card(card_info: str) -> str:
    """Функция маскировки карты или счета пользователя"""

    if "Счет" in card_info:
        return get_mask_account(card_info)
    else:
        return get_mask_card_number(card_info)

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))

#    if "Счет" in card_info:
#        return f"{card_info[0:5]}**{card_info[-4:]}"
#    else:
#        return f"{card_info[:-12]} {card_info[-12:-10]}** ****{card_info[-4:]}"

# Visa Platinum 7000792289606361
# Счет 73654108430135874305


def get_date(date: str) -> str:
    """Функция вывода даты"""


    date_format = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date
#    return f"{date[8:10]},{date[5:7]},{date[0:4]}"


print(get_date("2024-03-11T02:26:18.671407"))
