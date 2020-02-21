"""
Ejercicio 19)
Escribe una función que encuentre el numero más grande entre 3 numeros.
"""
mi_lista = [5, 100, 701]

def bigger (mi_lista):
    number_bigger = 0
    for digit in mi_lista:
        if digit >= number_bigger:
            number_bigger = digit
    return number_bigger

numero_mayor = bigger(mi_lista)
print(numero_mayor)