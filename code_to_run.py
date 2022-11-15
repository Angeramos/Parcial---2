from Clases.movies import Movies
from Clases.teatro import Teatro 
from Clases.tickets import Tickets 
from Clases.user import User

"""ingresamos  nuestro nombre"""
Anghely = User

"""aquí se crean las peliculas disponibles y su respectiva hora"""
"""La hora está en formato de 24"""
pelicula1 = Movies("Alicia",22) 
pelicula2 = Movies("TopGun", 19)
pelicula3 = Movies("SpiderMan", 9)

"""Aquí se crea la lista con las peliculas"""
peliculas= {"Alicia":pelicula1, "TopGun":pelicula2, "SpiderMan":pelicula3}

"""Aquí creamos el teatro (Que tiene mi nombre)"""
Ang = Teatro(peliculas)

"""Aquí compramos la cantidad de tiquetes que querramos, con la respectiva pelicula y cupos que escojamos"""
Ang.comprar_tickets("Alicia", 3, [2,3,4], "vip")


"""aquí se muestran los cupos disponibles"""
Ang.show_cupos("Alicia")

"""Aquí el diccionario que guarda a los usuarios y su silla preferida"""
usuarios = {"Anghely": 3, "José Posada": 1}

Anghely.Comprobar_user (usuarios, Anghely)