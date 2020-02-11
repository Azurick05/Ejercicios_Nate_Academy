
numero_multiplicar = int(input("Introduzca el numero a multiplicar: "))
primer_numero = int(input("Introduzca el primer numero del rango: "))
segundo_numero = int(input("Introduzca el segundo numero del rango: "))

for multiplo in range(primer_numero,segundo_numero + 1):
    print("{} x {} = {}".format(numero_multiplicar, multiplo, numero_multiplicar*multiplo))

print("Se ha acabado la multiplicacion." )