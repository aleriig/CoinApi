import requests

api_key = "D3B23BBC-48BC-477B-B842-1BC9796DB7F4"
headers = {
    'X-CoinAPI-Key' : api_key
}

another_exchange = "S"
while another_exchange.upper() == "S":

    origin_coin = input("Que moneda quieres cambiar?: ")
    destination_coin = input("Que moneda quieres obtener?: ")

    url = f"http://rest.coinapi.io/v1/exchangerate/{origin_coin}/{destination_coin}"
    response = requests.get(url, headers=headers)
    exchange_rate = response.json()
    exchange = exchange_rate["rate"]
    print("Un {} vale como {:,.2f} {}".format(exchange_rate["asset_id_base"], exchange_rate["rate"], exchange_rate["asset_id_quote"]))

    another_exchange = ""
    while another_exchange.upper() not in ("S", "N"): 
        another_exchange = input("Quieres hacer mas cambios de moneda?: (S/N) ")