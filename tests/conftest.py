import pytest


@pytest.fixture
def card_number() -> str:
    return "7000 79** **** 6361"


@pytest.fixture
def card_info() -> str:
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def account_info() -> str:
    return "Счет **4305"


@pytest.fixture
def account_number() -> str:
    return "**4305"


@pytest.fixture
def mask_account_card_info() -> str:
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def mask_account_check_info() -> str:
    return "Счет **4305"


@pytest.fixture
def check_date() -> str:
    return "11.03.2024"


@pytest.fixture
def check_state() -> list[dict[str, str | int] | dict[str, str | int]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def date_filtered() -> list[dict[str, str | int] | dict[str, str | int]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def same_date() -> list[dict[str, str | int] | dict[str, str | int]]:
    return [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-09-12T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]


@pytest.fixture
def incorrect_date_format() -> list[dict[str, str | int] | dict[str, str | int]]:
    return [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "03072019T18:35:29.512364"},
    ]
