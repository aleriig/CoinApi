import requests
# subir la api_key al repo si es publico, es una mala practica ya que cualquiera podria usarla
api_key = "D3B23BBC-48BC-477B-B842-1BC9796DB7F4"
headers = {
    'X-CoinAPI-Key' : api_key
}
api_url = "http://rest.coinapi.io"
# el endpoint o ruta lo separamos de la URL para consultar varias rutas y no tener que cambiar todo
endpoint = "/v1/assets"

url = api_url + endpoint

response = requests.get(url, headers=headers)
# para comprobar si el response es correcto
code = response.status_code

if code == 200:
    print("Las monedas disponibles son: ")
    # convertimos a json para interpretarlo en python como un diccionario
    response_json = response.json()
    
    for coin in response_json:
        if coin ["asset_id"].startswith("EUR"):    
            print(coin["asset_id"], coin["name"])
else:
    print("La peticion a la API ha fallado")
    print(f"Codigo del error {code}")
    print(f"Razon del error {response.reason}")
    print(response.text)
