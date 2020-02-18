"""
Ejercicio 13)
Crear un programa que cambie todas las ‘A’ o ‘a’ por
la string ‘VACA’ de una string introducida por el usuario.
"""

frase_input = input("Introduzca una frase: ")

cambio_mayuscula = frase_input.replace("A", "VACA")
cambio_minuscula = cambio_mayuscula.replace("a", "VACA")

print(cambio_minuscula)