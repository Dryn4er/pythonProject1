import json

from urllib3 import request

from src.utils import get_summ, get_transactions_data
from src.external_api import conversion_currency

from unittest.mock import patch, MagicMock
import requests

@patch('src.external_api.requests.request')
def test_amount_exchange(mock_get):
    mock_get.return_value.json.return_value = {

        "date": "2018-02-22",

        "historical": "",

        "info": {

            "rate": 148.972231,

            "timestamp": 1519328414

        },

        "query": {

            "amount": 20,

            "from": "USD",

            "to": "RUB"

        },

        "result": 3724.305775,

        "success": True

    }
    assert conversion_currency(amount=25, from_curr="USD", to_curr="RUB") == 3724.305775
    mock_get.assert_called_once_with('GET', 'YOUR_API_URL', params={'amount': 25, 'from': 'USD', 'to': 'RUB'})


@patch('builtins.open')
def test_get_transactions_data(mock_data: MagicMock):
    mock_open = mock_data.return_value.__enter__.return_value
    mock_open.read.return_value = json.dumps([{"test": "test"}])
    assert get_transactions_data("/Users/Admin/PycharmProjects/pythonProject1/data/operations.json") == [{"test": "test"}]
    mock_open.read.return_value = json.dumps([{}])
    assert get_transactions_data("/Users/Admin/PycharmProjects/pythonProject1/data/operations.json") == [{}]
    mock_open.read.return_value = ""
    assert get_transactions_data("/Users/Admin/PycharmProjects/pythonProject1/data/operations.json") == []


