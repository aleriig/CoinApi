from tkinter import ttk

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
    def __init__(self, father):
        super().__init__(father, width=400, height=400)
        self.create_controllers()

    def create_controllers(self):
        example_label = ttk.Label(self)
        example_label.grid(row=0, column=0)
        