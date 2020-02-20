"""
Ejercicio 18)
Crear un programa que guarde e imprima varias listas con todos los números que estén
dentro de una lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.
"""

multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

respuesta = input("Introduzca numeros enteros para decirle cuales son multiplo de 2, 3, 5 y de 7 (FIN para terminar): ").upper()

while respuesta != "FIN":
    if int(respuesta) % 2 == 0:
        multiplos_dos.append(respuesta)
    if int(respuesta) % 3 == 0:
         multiplos_tres.append(respuesta)
    if int(respuesta) % 5 == 0:
        multiplos_cinco.append(respuesta)
    if int(respuesta) % 7 == 0:
        multiplos_siete.append(respuesta)
    respuesta = input("Introduzca numeros enteros para decirle cuales son multiplo de 2, 3, 5 y de 7 (FIN para terminar): ").upper()


print(multiplos_dos)
print(multiplos_tres)
print(multiplos_cinco)
print(multiplos_siete)