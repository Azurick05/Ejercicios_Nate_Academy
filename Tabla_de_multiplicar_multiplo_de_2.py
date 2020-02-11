
numero_elegido = int(input("Introduzca el numero a multiplicar y le devolvere los multiplos de 2: "))
resto = 0

for multiplo in range(1,11):
    resto = (multiplo*numero_elegido) % 2
    if resto == 0:
        print("{} * {} = {}".format(numero_elegido, multiplo, numero_elegido*multiplo))

print("Se ha acabado la multiplicacion.")