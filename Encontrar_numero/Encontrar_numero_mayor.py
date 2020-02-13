
tabla_de_numeros = []
numero_del_usuario = ""

while len(tabla_de_numeros) < 5:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = (input("Introduzca un número: "))
    tabla_de_numeros.append(numero_del_usuario)
    numero_del_usuario = ""
    print("Numero introducido.")

grande = tabla_de_numeros[0]
print("La tabla es esta: {}".format(tabla_de_numeros))

for numero in tabla_de_numeros:
    if numero > grande:
        print("El numero {} es mayor que el {}".format(numero,grande))
        grande = numero

print("El numero mas grande es el {}".format(grande))