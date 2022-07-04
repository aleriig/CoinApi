from tkinter import *

from .models import CryptoModel
from .views import CryptoView, CryptoViewTK


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


class CryptoControllerTk(Tk):
    def __init__(self):
        super().__init__()
        # Hacemos un callback, metiendo una funcion como un parametro para recibir de Views y sin llamarla
        self.view = CryptoViewTK(self, self.calculate_exchange)
        self.models = CryptoModel()

    def run(self):
        self.mainloop()

    def calculate_exchange(self):
        """ 
        - Recoge los datos de la vista y los pasa al modelo.
        - Pide el cambio al modelo y le pasa el resultado a la     vista.
        """
        print("Hola soy calcular cambio CryptoControllerTK")