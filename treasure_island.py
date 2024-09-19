print("Bienvenido al concurso de los 100 €")
name = input("Cual es tu nombre: ")

print(f"Hola {name}, preparado para ganar dinero \n Debes responder correctamente las siguientes preguntas: ")



# 1ºPASO

primer_paso = input("a que lado quieres ir: izquierda o derecha: ").lower()

if primer_paso == "izquierda" or primer_paso == "izq":
    print("Es correcto has ido por el lado correcto")
    print("Ahora quieres ir abajo o arriba")
    segundo_paso = input("Ellige abajo o arriba: ")
    if segundo_paso == "arriba":
        print("Has acertado!!!")
    else:
        print("GAME OVER")
elif primer_paso == "derecha":
    print("GAME OVER")
else:
    print("Has metido una respuesta equivocada")