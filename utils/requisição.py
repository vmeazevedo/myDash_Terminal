import requests
import json

def buscar_dados(coin):
    request = requests.get(f"https://www.mercadobitcoin.net/api/{coin}/ticker")
    payload = json.loads(request.content)
    coin = payload['ticker']['last']
    return float(coin)