#Piedra, papel y tijera

import random

opciones = ["piedra" , "papel" , "tijera"]
your_option = input("elige entre: piedra, papel o tijera: ")

opcion_aleatoria = random.choice(opciones)

while your_option == opcion_aleatoria:
    print("Has empatado")
    your_option = input("elige entre: piedra, papel o tijera: ")
    


if your_option == "piedra" and opcion_aleatoria == "tijera":
    print("HAS GANADO!!!!")
elif your_option == "piedra" and opcion_aleatoria == "papel":
    print("HAS PERDIDO, SORRYYYY")
elif your_option == "papel" and opcion_aleatoria == "piedra":
    print("HAS GANADO!!!!")
elif your_option == "papel" and opcion_aleatoria == "tijera":
    print("HAS PERDIDO, SORRYYYY")
elif your_option == "tijera" and opcion_aleatoria == "papel":
    print("HAS GANADO!!!!")
elif your_option == "tijera" and opcion_aleatoria == "piedra":
    print("HAS PERDIDO, SORRYYYY")
else:
    print("Has incluido algun caracter invalido")
