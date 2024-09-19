# #Realiza un programa que pida una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

# frase = input("Dime una frase: ").lower()
# letra = input("Dime una letra: ").lower()

# while len(letra) > 1:
#     print("solo puedes meter una letra ERROR!!!")
#     letra = input("Dime una letra: ").lower()
    

# frase_lista = list(frase)
# numero = 0

# for letras in frase_lista:
#     if letras == letra:
#         numero += 1
        

# print(f"El numero de veces que aparece la letra en tu frase es {numero}")



# Realiza un programa que te pida un número y te muestre un triangulo rectángulo como el siguiente, por ejemplo si metes 9:

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

numero = 9

lista_vacia = []

for x in range(1, numero + 1 , 2):
    lista_vacia.append(str(x))
    print(' '.join(reversed(lista_vacia)))
    
    
    

    