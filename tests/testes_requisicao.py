import requests
import pytest


LINK_CONSULTA = 'https://www.mercadobitcoin.net/api/BTC/ticker/'


def test_code_requisition():
    try:
        request = requests.get(LINK_CONSULTA)
        if request.status_code == 403:
            raise ConnectionError('Forbidden')

        if request.status_code == 200:
            print('Conexão realizada com sucesso')

    except ConnectionError:
        print('Não foi possível obter resposta')




