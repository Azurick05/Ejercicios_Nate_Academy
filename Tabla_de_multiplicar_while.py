
numero_a_multiplicar = int(input("Introduzca el numero a multiplicar: "))

multiplicador = 5
resultado = 0

while multiplicador < 16:
    resultado = multiplicador * numero_a_multiplicar
    print("{} x {} : {}".format(numero_a_multiplicar, multiplicador, resultado))
    multiplicador += 1

print("Ha terminaado la multiplicacion.")