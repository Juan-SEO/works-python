# En el boletín las notas no son numéricas, de 0,1 y 2 deficiente, de 3 y 4, insuficiente, 5 y 6 aprobado 7 y 8 notable y 9 y 10 sobresalientes. 
# Realiza un programa que pregunte al alumno por su nota numérica y muestre la nota que corresponde en el boletín.

# print("Comprobador de notas: ")
# nota = int(input("cual es tu nota: "))

# if nota >= 0 and nota <= 2:
#     print("Deficiente ")
# elif nota >=3 and nota <=4:
#     print("insuficiente")
# elif nota >=5 and nota <=6:
#     print("aprobado")
# elif nota >=7 and nota <=8:
#     print("notable")
# elif nota >=9 and nota <=10:
#     print("sobresalientes")
# else:
#     print("Has metido una nota erronea")


#Realiza un programa que te pida un número y te muestre un triangulo rectángulo, por ejemplo si metes 5:--------------------------------------------------------------------

# numbers = int(input("Dime un numero:   "))
# numbers = 7
# imprimir = []

# for number in range(numbers + 1):
#     imprimir.append(str(number))
#     print(" ".join(imprimir))


# Realiza un programa que pida una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.-----------------------------------------

# palabra = input("Dime una palabra: ")
# palabra_lista = list(palabra)

# palabra_lista.reverse()

# print(palabra_lista)





# Realiza un programa que almacene las asignaturas del curso en una lista y las muestre por pantalla. Las asignaturas serán introducidas por teclado.

# asignaturas = []

# while True:
#     asignatura = input("Dime una asignatura o pulsa 0 para salir: ")
#     if asignatura == "0":
#         break
#     else:
#         asignaturas.append(asignatura)

# print("Las asignaturas disponibles: ")

# for asignatura in asignaturas:
#     print(asignatura)















# numeros = int(input("Dime un numero: "))
# numeros_f=[]

# for x in range(1,numeros + 1):
#     numeros_f.append(x)
#     numeros_f.reverse()
#     print(" ".join([str(x) for x in numeros_f]))



# class Dice:
#     def __init__(self, size = 6):
#         print("Creating object")
#         self.size = size
#         print(f"Size: {size}")
    
#     def throw(self):
#         print("To be implemented")

# dice = Dice()
# dice.throw()
    



# word = input("dime una palabra")

# for x in range(1,11):
#     print(word)


#ealiza un programa que pregunte tu edad y muestre por pantalla todos los años que has cumplido (desde 1 hasta tu edad).

# edad = int(input("cual es tu edad? "))

# for x in range(1, edad + 1):
#     print(x)

# Realiza un programa que me imprima los 100 primeros números impares y me muestre su suma.
# for x in range(1,101):
#     if x % 2 == 1:
#         print(x)



# numero_1 = int(input("Dime tu primer numero: "))
# numero_2 = int(input("Dime tu segundo numero: "))

# print("los numeros que hay entre los dos numeros proporcionados son: ")
# for x in range(numero_1,numero_2):
#     print(x)

# print("Los numeros que hay ente los dos son:" + str(len(range(numero_1,numero_2))))


usuario = input("Dime el nombre de usuario: ")
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
simbolos = ["!", "-"]

# Verificar si al menos un número está en el usuario
contiene_numero = any(num in usuario for num in numeros)

# Verificar si al menos un símbolo está en el usuario
contiene_simbolo = any(simbolo in usuario for simbolo in simbolos)

if len(usuario) <= 8 or not contiene_numero or not contiene_simbolo:
    print("Has creado mal el usuario")
else:
    print("Está bien")
