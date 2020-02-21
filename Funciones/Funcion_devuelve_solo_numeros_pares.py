"""
Ejercicio 21)
Escribe una función que reciba una lista de números y devuelva otra pero conteniendo solo los números pares.
devolver_pares([1, 2, 3, 4, 5, 6])
[2, 4, 6]
"""

lista_numeros = [1, 2, 3, 4, 5, 6]

def numeros_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return  pares

lista_final = numeros_pares(lista_numeros)
print(lista_final)