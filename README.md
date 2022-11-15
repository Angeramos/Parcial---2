# *DESCRIPCIÓN*
## *Movie Tickets* 

    Se tiene un teatro donde se quieren vender tiquetes para diferentes películas, el usuario debe poder seleccionar la película, la hora, la posición, y el numero de tiquetes que desea comprar. Existen dos tipos de tiquetes, VIP y regular. Se debe llevar una cuenta de los cupos disponibles. Se pueden recibir múltiples usuarios, los usuarios se pueden registrar y se debe guardar su preferencia de asiento. 

# *Cómo correr el código*

    En el Code_to_run, están colocadas las peliculas disponibles (las puede cambiar si desea), y el número de tiquetes que desea comprar, con sus respectivas posiciones en la pelicula que escoja, al correr el código le debe decir si su venta fue realizada, y los cupos/asientos que quedan disponibles los cuales tendrán un "0". 

# *Explicación UML*x

    Cree una clase teatro, que sería la principal que recibe el diccionario con los nombres de las peliculas, la clase movies la cual se compone de la clase Tickets donde se recibe el nombre y el tiempo de la pelicula. 
    Luego una clase abstracta Tickets, de la cual heredan VIP y regular, en cada ticket se guarda como atributo la posicion, la hora, y el nombre de la pelicula. Por ultimo la clase usuario qu erecibe un diccionario donde se relaciona el nombre de la persona y su posicion favorita.

