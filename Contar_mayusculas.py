
input_frase = input("Introduzca una frase, el programa le dara el numero de mayusculas que use: ")

contador_mayusculas = 0

for letra in input_frase:
    if letra == letra.upper() and letra != " " and letra != "," and letra != ".":
        contador_mayusculas += 1

print("Mayusculas: {}".format(contador_mayusculas))