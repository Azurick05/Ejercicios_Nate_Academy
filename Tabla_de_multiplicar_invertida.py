
numero_multiplicar = int(input("Introduzca el numero a multiplicar: "))

tabla = []
posicion_tabla = -1

for multiplo in range(1,11):
    tabla.append(multiplo)

while posicion_tabla > -11:
    print("{} x {} = {}".format(numero_multiplicar, tabla[posicion_tabla], numero_multiplicar*tabla[posicion_tabla]))
    posicion_tabla -= 1