from typing import Any


def filter_by_state (list_to_filter: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    filtered_list = []
    for i in list_to_filter:
        if i["state"] == state:
            filtered_list.append(i)
    return filtered_list