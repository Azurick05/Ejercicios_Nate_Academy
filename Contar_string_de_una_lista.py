lista_input = []

entrada_usuario = input("Introduzca palabras y le diré la longitud de cada palabra (escriba FIN para terminar): ")

while entrada_usuario != "FIN":
    lista_input.append(len(entrada_usuario))
    entrada_usuario = input("Introduzca otra palabras (escriba FIN para terminar): ")

print(f"{lista_input}")