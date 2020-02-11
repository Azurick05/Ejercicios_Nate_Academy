tabla_de_numeros = []
numero_del_usuario = ""
seguir = "Y"
suma = 0

while seguir == "Y":
    while not numero_del_usuario.isdigit():
        numero_del_usuario = (input("Introduzca un número: "))
    tabla_de_numeros.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Numero introducido.")
    seguir = input("¿Quieres seguir metiendo números? (Y/N): ").upper()
    if seguir != "Y" and seguir != "N":
        print("No se lo que has puesto pero considero que no quieres meter mas numeros.")
        seguir = "N"

for numero in tabla_de_numeros:
    suma = suma + numero

print("{}".format(tabla_de_numeros))
print("La media de los numeros introducidos es: {}".format(suma/len(tabla_de_numeros)))