"""
Ejercicio 16)
Realizar el FizzBuzz con las mismas reglas pero
en el caso que el numero sea divisible entre 3 y 5, cambiar el texto por «Bazinga».
"""

enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 16, 17, 20, 30]

contador = 0

for digitos in enteros:
    if digitos % 3 == 0 and digitos % 5 == 0:
        enteros[contador] = "Bazinga"
    elif digitos % 3 == 0:
        enteros[contador] = "Fizz"
    elif digitos % 5 == 0:
        enteros[contador] = "Buzz"
    contador += 1

print(enteros)