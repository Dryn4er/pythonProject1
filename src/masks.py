from typing_extensions import Union
import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_info: str) -> str:
    """Функция, которая маскирует номер карты"""

    logger.info(f"Получаем информацию по карте/счету")
    if card_info.isdigit() and len(card_info) == 16:
        logger.info(f"Ваша карта: {card_info[0:4]} {card_info[4:6]}** **** {card_info[12:16]}")
        return f"{card_info[0:4]} {card_info[4:6]}** **** {card_info[12:16]}"
    elif card_info.isdigit() and len(card_info) != 16 and len(card_info) != 20:
        logger.error(f"Введите корректный номер карты/счета")
        raise Exception("Введите корректный номер карты/счета")
    elif card_info.isdigit() and len(card_info) == 20:
        logger.info(f"Ваш счет: **{card_info[-4:]}")
        return f"**{card_info[-4:]}"
    elif card_info is None:
        logger.error(f"Введите номер карты/счета")
        return "Введите номер карты/счета"

    if not card_info.isdigit():
        numbers = []
        for i in card_info:
            if i.isdigit():
                numbers.append(i)
            else:
                continue
        if len(numbers) == 16:
            logger.info(f"Ваша карта: {card_info[:-12]} {card_info[-12:-10]}** **** {card_info[-4:]}")
            return f"{card_info[:-12]} {card_info[-12:-10]}** **** {card_info[-4:]}"


#        else:
#            raise Exception("Введите корректный номер карты/счета")


def get_mask_account(card_info: Union[int, str]) -> str:
    """Функция, которая маскирует номер счета"""

    logger.info(f"Ваш счет: {card_info[0:5]}**{card_info[-4:]}")
    return f"{card_info[0:5]}**{card_info[-4:]}"


# print(get_mask_card_number(card_info))
# print(get_mask_account(card_info))
