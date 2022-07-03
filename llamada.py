import requests

api_key = "D3B23BBC-48BC-477B-B842-1BC9796DB7F4"
headers = {
    'X-CoinAPI-Key' : api_key
}
api_url = "http://rest-sandbox.coinapi.io"
# el endpoint o ruta lo separamos de la URL para consultar varias rutas y no tener que cambiar todo
endpoint = "/v1/exchanges"

url = api_url + endpoint

response = requests.get(url, headers=headers)
# para comprobar si el response es correcto
code = response.status_code

if code == 200:
    print("El resultado de la consulta es: ")
    print(response.text)
else:
    print("La peticion a la API ha fallado")
    print(f"Codigo del error {code}")
    print(f"Razon del error {response.reason}")
    print(response.text)
