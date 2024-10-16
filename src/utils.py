import json
from typing import Any

from src.external_api import conversion_currency


def get_transactions_data(file: str) -> list[dict]:
    """Возвращает список словарей с данными о транзакциях"""

    emtpy_list = []
    try:
        with open(file, encoding="UTF-8") as f:
            try:
                transaction_data = json.load(f)
            except json.JSONDecodeError:
                return  emtpy_list
    except FileNotFoundError:
        return emtpy_list
    return transaction_data


def get_summ(data: Any) -> Any:
    """Возвращает сумму транзакций"""

    data = get_transactions_data("/Users/Admin/PycharmProjects/pythonProject1/data/operations.json")
    conv_list = []
    summ = []
    for i in data:
        if len(i) == 0:
            continue
        elif i["operationAmount"]["currency"]["code"] != 'RUB':
            conversion_currency("RUB", i["operationAmount"]["currency"]["code"], i["operationAmount"]["amount"])
        conv_list.append(i["operationAmount"]["amount"])
    for i in conv_list:
        summ.append(float(i))
    return sum(summ)


if __name__ == '__main__':
    get_transactions_data("/Users/Admin/PycharmProjects/pythonProject1/data/operations.json")
    print(get_summ(get_transactions_data))
