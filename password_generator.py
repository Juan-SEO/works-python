#Password Generator Project
import random

#Variables para crear las contraseñas::
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Bienvenido al generador de contraseñas automatico:  ")


#Variables que guardan las especificaciones del usuario para la creacion de la contraseña:
numero_letras = int(input("Cuantas letras quieres en tu contraseña?? "))
numero_numeros = int(input("Cuantas numeros quieres en tu contraseña?? "))
numero_simbolos = int(input("Cuantos simbolos quieres en tu contraseña?? "))

#Varianbles para gauirdar los caracteres genrados en cada punto
letter_final = []
number_final = []
symbols_final = []

#1º Generar las letras aleatorias
for x in range(numero_letras):
    letter_final += random.choice(letters)
    

# 2º Generar numeros aleatorios
for x in range(numero_numeros):
    number_final += random.choice(numbers)
    

# 3º Generar numeros aleatorios
for x in range(numero_simbolos):
    symbols_final += random.choice(symbols)
    

# Combinar todas las listas
final = letter_final + number_final + symbols_final

# Mezclar la lista combinada
random.shuffle(final)

# Convertir la lista mezclada en una cadena
final_string = ''.join(final)

print("Tu contraseña generada es:", final_string)