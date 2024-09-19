import random


aleatory = random.randint(1,10)
adivinar = 0


while aleatory != adivinar:
    adivinar = int(input("Adivina el numero del 1 al 10:  "))
    print("Has fallado, vuelve a probar")


print("Has acertado!!!!!")

