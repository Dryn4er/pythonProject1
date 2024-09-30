from typing import Any


def filter_by_state(list_to_filter: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция возвращает только словари с необходимым ключом"""
    filtered_list = []
    for i in list_to_filter:
        if i["state"] == state:
            filtered_list.append(i)
        else:
            continue
    return filtered_list


def sort_by_date(list_to_sort: list[dict[str, Any]], revers: bool = True) -> list[dict[str, Any]]:
    """Функция сортирует словари по убыванию согласно дате"""
    sorted_list = sorted(list_to_sort, key=lambda x: x["date"], reverse=revers)
    return sorted_list


if __name__ == "__main__":
    list_to_filter = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(list_to_filter))
    list_to_sort = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(sort_by_date(list_to_sort))
