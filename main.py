
factura=float(input("dime el valor de la factura: "))
porcentaje=int(input("cuanto procentaje quereis dar de propina: 10 12 o 15 "))*0.01
personas=int(input("cuantas personas van a pagar la propina: "))

# El valor absoluto de la propina
propina = factura * porcentaje


valor_t=factura + propina

reparto= round(valor_t/personas , 2)



if reparto < 25:
    print("Hemos conseguido ahorrar")
else:
    print("No ahorramos ni pa tras")