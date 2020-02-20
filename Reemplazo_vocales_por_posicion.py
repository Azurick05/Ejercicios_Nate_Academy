"""
Ejercicio 15)
Crear un programa que cambia las vocales por su numero de aparición.
Por ejemplo la string «aurora boreal» se convertiría en «12r3r4 b5r67l»
"""

frase = "aurora boreal"

aparicion = 1
vocales = ["a", "e", "i", "o", "u"]

for letra in frase:
    for vocal in vocales:
        if vocal == letra:
            frase = frase.replace(letra,str(aparicion),1)
            aparicion += 1


print(frase)