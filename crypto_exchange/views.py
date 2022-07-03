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

        