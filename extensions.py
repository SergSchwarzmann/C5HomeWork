import requests
import json
from config import keys

class APIExeptions(Exception):
  pass

class CurrecyConverter:
  @staticmethod
  def get_price(base:str, quote:str, amount:str):

    if base == quote:
      raise APIExeptions(f'Cannot convert same currency: {base}.')

    try:
      base_ticker = keys[base]
    except KeyError:
      raise APIExeptions(f'Cannot find currency {base}.')

    try:
      quote_ticker = keys[quote]
    except KeyError:
      raise APIExeptions(f'Cannot find currency {quote}.')

    try:
      amount = float(amount)
    except KeyError:
      raise APIExeptions(f'Cannot find quantity {amount}.')


    url = f"https://api.apilayer.com/fixer/convert?to={quote_ticker}&from={base_ticker}&amount={amount}"

    payload = {}
    headers= {
      "apikey": "gxjqGA14UovudVoI3FUbfJE0cLM5ORtu"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    # res = response.text
    # print(res)

    total = json.loads(response.content)['result']
    u = json.loads(response.content)['info']
    rate = u['rate']

    return total, rate
