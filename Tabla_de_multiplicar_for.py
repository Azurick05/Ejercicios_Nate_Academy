
numero_multiplicar = int(input("Introduzca el numero a multiplicar: "))

for multiplo in range(5,16):
    print("{} x {} = {}".format(numero_multiplicar, multiplo, numero_multiplicar*multiplo))

print("Se ha acabado la multiplicacion." )