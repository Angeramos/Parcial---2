from abc import ABC, abstractmethod

class Tickets (ABC): 
    @abstractmethod
    def __init__(self, position:int, time:float, movie:str) -> None:
        self.Position 
        self.time
        self.Movie 
        super().__init__()
        
