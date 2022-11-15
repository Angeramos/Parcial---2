from tickets import Tickets 

class Vip(Tickets):
    def __init__(self, position: int, time: float, movie: str) -> None:
        super().__init__(position, time, movie)
    def comprar_comida() -> None:
        print ("Con este ticket, tiene derecho a una comida gratis")


