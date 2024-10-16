import os
from typing import Any

import requests
from dotenv import load_dotenv

def conversion_currency(to_curr: Any, from_curr: Any, amount: Any) -> Any:
    load_dotenv('.env')
    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_curr}&from={from_curr}&amount={amount}"
    headers = {"api_key": api_key}
    responce = requests.get(url, headers=headers)
    result = responce.json
    return result


if __name__ == '__main__':
    print(conversion_currency("RUB", "USD",  "200000"))