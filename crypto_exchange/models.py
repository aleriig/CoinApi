# El model llamara a la API y se encargará de los datos
import requests
# El "." es equivalente a escribir el nombre de la carpeta donde estamos, en este caso "crypto_exchange"
from . import API_KEY

# Hacemos una clase Error con Exception para hacer un error propio nuestro, no uno generico
class APIError(Exception):
    pass

class CryptoModel:
    """ 
    - origin_coin 
    - destination_coin  
    - exchange_rate 
    - check_exchange_rate

    """

    def __init__(self):
        """
        COnstruye un objeto con las monedas origen y destino y el cambio obtenido desde CoinAPI inicializado a cero.
        
        """
        self.origin_coin = ""
        self.destination_coin = ""
        self.exchange = 0.0
        

    def check_exchange(self):
        """
        Consulta el cambio entre la moneda origen y la moneda destino utilizando la API REST CoinAPI

        """
        headers = {
            'X-CoinAPI-Key' : API_KEY
        }
        url = f"http://rest.coinapi.io/v1/exchangerate/{self.origin_coin}/{self.destination_coin}"
        response = requests.get(url, headers=headers)
        
        # verificamos la respuesta
        if response.status_code == 200:
            # guardo el cambio obtenido
            self.exchange = response.json()["rate"]
        else:
            raise APIError("Ha ocurrido un error {} {} al consultar la API".format(response.status_code, response.reason))