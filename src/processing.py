from typing import Any


def filter_by_state(list_to_filter: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    filtered_list = []
    for i in list_to_filter:
        if i["state"] == state:
            filtered_list.append(i)
    return filtered_list


def sort_by_date(list_to_sort: list[dict[str, Any]], revers: bool = True) -> list[dict[str, Any]]:
    sorted_list = sorted(list_to_sort, key=lambda x: x['date'], reverse=revers)
    return sorted_list
