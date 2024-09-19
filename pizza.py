#Calculadora de precios para pizzeria


print("Bienvenidos a Pizza Juan")
size = input("Qué tamaño de pìzza deseas S M o L? ")
pepperoni = input("Quieres peperroni: S/N ")
extra_cheese = input("Quiertes queso si o no? ")

#Calculo de precio de la pizza
if size == "S":
    precio = 15
    if pepperoni == "S":
        precio += 2
elif size == "M":
    precio = 20
    if pepperoni == "S":
        precio += 3
else:
    precio = 25
    if pepperoni == "S":
        precio += 3


if extra_cheese == "S":
    precio += 1
else:
    precio += 0

print(f"El precio de la pizza es: {precio}")