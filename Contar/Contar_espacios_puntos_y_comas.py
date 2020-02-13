
input_frase = input("Introduzca una frase y el programa le contara el numero de espacios, puntos y comas de este: ")

espacio_contador = 0
puntos_contador = 0
comas_contador = 0

for letra in input_frase:
    if letra == " ":
        espacio_contador += 1
    elif letra == ".":
        puntos_contador += 1
    elif letra == ",":
        comas_contador += 1

print("Espacios: {}".format(espacio_contador))
print("Puntos: {}".format(puntos_contador))
print("Comas: {}".format(comas_contador))