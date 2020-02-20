"""
Ejercicio 17)
Crear un programa que encuentre el numero más grande de una lista (sin usar la función max).
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 70, 10, 13, 15, 16, 17, 20, 30]

mayor = 0

for entero in numeros:
    if entero > mayor:
        mayor = entero

print(mayor)