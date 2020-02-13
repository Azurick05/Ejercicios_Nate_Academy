
numero_a_multiplicar = int(input("Introduzca el numero a multiplicar: "))

multiplicador = 5

while multiplicador < 16:
    print("{} x {} : {}".format(numero_a_multiplicar, multiplicador, numero_a_multiplicar*multiplicador))
    multiplicador += 1

print("Ha terminaado la multiplicacion.")