from tickets import Tickets 

class Regular(Tickets):
    def __init__(self, position: int, time: float, movie: str) -> None:
        super().__init__(position, time, movie)
        pass