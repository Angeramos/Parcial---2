class Teatro: 
    def __init__(self, movies:dict):
        self.movies = movies 
    def comprar_tickets(self, name:str, cant:int, position:list, tipo:str)->None:
        if tipo != "vip":
            raise Exception ("Su boleta es regular, y no tiene derecho a comida")
        else:
            print ("tiene derecho a una comida gratis")
        pelicula = self.movies[name]
        if cant > len(pelicula.cupos):
            raise Exception ("excede el número de cupos")
        else:
            for p in position:
                if pelicula.cupos[p] == 0:
                    pelicula.cupos[p] = 1
                else:
                    raise Exception("esta silla está ocupada")
            print ("Venta realizada")
    def show_cupos(self, name:str) -> None:
        pelicula = self.movies[name] 
        print(pelicula.cupos)