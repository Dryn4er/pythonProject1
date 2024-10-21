import json
from typing import Any
import logging
from src.external_api import conversion_currency

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/utils.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_data(file: str) -> list[dict]:
    """Возвращает список словарей с данными о транзакциях"""

    logger.info(f'Получаем список словарей')
    emtpy_list = []
    try:
        with open(file, encoding="UTF-8") as f:
            try:
                logger.info(f'Список словарей получен')
                transaction_data = json.load(f)
            except json.JSONDecodeError:
                logger.error(f'Пустой список')
                return  emtpy_list
    except FileNotFoundError:
        logger.error(f'Пустой список')
        return emtpy_list
    return transaction_data


def get_summ(data: Any) -> Any:
    """Возвращает сумму транзакций"""

    logger.info(f'Получаем информацию о транзакциях')
    data = get_transactions_data("/Users/Admin/PycharmProjects/pythonProject1/data/operations.json")
    conv_list = []
    summ = []
    logger.info(f'Суммируем транзакции')
    for i in data:
        if len(i) == 0:
            continue
        elif i["operationAmount"]["currency"]["code"] != 'RUB':
            conversion_currency("RUB", i["operationAmount"]["currency"]["code"], i["operationAmount"]["amount"])
        conv_list.append(i["operationAmount"]["amount"])
    for i in conv_list:
        summ.append(float(i))
    logger.info(f'Сумма транзакций: {sum(summ)}')
    return sum(summ)


if __name__ == '__main__':
    get_transactions_data("/Users/Admin/PycharmProjects/pythonProject1/data/operations.json")
    print(get_summ(get_transactions_data))
