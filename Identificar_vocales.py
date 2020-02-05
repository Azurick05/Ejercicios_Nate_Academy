
input_frase = input("Introduzca una frase: ")

referencia = ["a", "e", "i" , "o", "u"]
contador_vocales = 0
vocales = []

for letra in input_frase:
    for vocal in referencia:
        if letra == vocal:
            vocales.append(letra)

print("Vocales: {}".format(vocales))