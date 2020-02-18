lista_inicial = ["hola", 2, "Andrés", 13, "", 66]

letras = []
numeros = []

for objeto in lista_inicial:
    if type(objeto) == type(""):
        letras.append(objeto)
    elif type(objeto) == type(1):
        numeros.append(objeto)

print(f"String{letras}, Numeros{numeros}")