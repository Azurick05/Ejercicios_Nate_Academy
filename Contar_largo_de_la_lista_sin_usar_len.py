tabla_de_numeros = []
numero_del_usuario = ""
contador = 0
seguir = "Y"

while seguir == "Y":
    while not numero_del_usuario.isdigit():
        numero_del_usuario = (input("Introduzca un número: "))
    tabla_de_numeros.append(numero_del_usuario)
    numero_del_usuario = ""
    print("Numero introducido.")
    contador += 1
    seguir = input("¿Quieres seguir metiendo números? (Y/N): ").upper()
    if seguir != "Y" and seguir != "N":
        print("No se lo que has puesto pero considero que no quieres meter mas numeros.")
        seguir = "N"

print("{}".format(tabla_de_numeros))
print("El largo de la lista es: {}".format(contador))