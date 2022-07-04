from tkinter import StringVar, ttk

from . import COINS

"""
    Models <=> Controllers <=> Views
    Models <////> Views (NUNCA hay comunicacion entre el model y el view directamente)

"""


class CryptoView:

    def __init__(self):
        pass

    def ask_coin(self):
        origin = input("Que moneda quieres cambiar?: ")
        destination = input("Que moneda quieres obtener?: ")
        return (origin, destination)

    def show_exchange(self, origin, destination, exchange):
        print("Un {} vale como {:,.2f} {}".format(origin, exchange, destination))

    def continue_exchange(self):
        another_exchange = input("Quieres hacer mas cambios de moneda?: (S/N) ")
        return another_exchange.upper()


class CryptoViewTK(ttk.Frame):
    def __init__(self, father, action):
        super().__init__(father, width=400, height=400, padding=20)
        self.button_functionality = action
        self.grid()
        self.create_controllers()

    def create_controllers(self):
        # entrada moneda origen
        self.origin = StringVar()
        origin_label = ttk.Label(self, text='Origin Coin')
        origin_label.grid(row=0, column=0)

        origin_combo = ttk.Combobox(self, values=COINS, textvariable=self.origin)
        origin_combo.grid(row=1, column=0)
        
        # entrada moneda destino
        destination_label = ttk.Label(self, text="Destination Coin")
        destination_label.grid(row=0,column=1)
        
        self.destination = StringVar()
        destination_combo = ttk.Combobox(self, values=COINS, textvariable=self.destination)
        destination_combo.grid(row=1, column=1)


        # label para la conversion
        self.exchange_label = ttk.Label(self, text="0.0",padding=20)
        self.exchange_label.grid(row=2, column=0, columnspan=2)

        # Entrada de botton de conversion. Con el command registramos el evento de clickar el boton
        self.convert_button = ttk.Button(self, text="Convert", command=self.button_functionality)
        self.convert_button.grid(row=3, column=1)

    def origin_coin(self):
        return self.origin.get()[:3]

    def destination_coin(self):
        return self.destination.get()[:3]


    def button_functionality(self):
        # Usamos el "get" para que el programa nos devuelva el valor de la variable en una cadena.
        print("La moneda origen es: ", self.origin_coin())
        print("La moneda destino es: ", self.destination_coin())
