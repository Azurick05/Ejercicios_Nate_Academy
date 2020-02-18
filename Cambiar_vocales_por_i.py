"""
Ejercicio 14)
Crear un programa que le repita al usuario lo que dice pero con todas las vocales cambiadas por i.
"""

frase_input = input("Introduzca una frase: ")

vocales = ["a", "e", "o", "u"]

for letra in vocales:
    frase_input = frase_input.replace(letra,"i")

print(frase_input)