from .models import CryptoModel
from .views import CryptoView

class CryptoController:

    def __init__(self):
        # instancio views and models
        self.model = CryptoModel()
        self.view = CryptoView()

    def check(self):
        another_exchange = "S"
        while another_exchange.upper() == "S":
            origin, destination = self.view.ask_coin()
            
            self.model.origin_coin = origin
            self.model.destination_coin = destination
            self.model.check_exchange()
            
            self.view.show_exchange(origin, destination, self.model.exchange)

            another_exchange = ""
            while another_exchange.upper() not in ("S", "N"):
                another_exchange = self.view.continue_exchange()