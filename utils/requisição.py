import requests
import json

from utils.consts import MENSAGEM_ERRO_CONSULTA, LINK_API


def buscar_dados(coin):
    try:
        request = requests.get(f"{LINK_API}/{coin}/ticker")

        if request.status_code != 200:
            return MENSAGEM_ERRO_CONSULTA
        else:
            payload = json.loads(request.content)
            coin = payload['ticker']['last']
            return float(coin)

    except ConnectionError:
        return MENSAGEM_ERRO_CONSULTA
