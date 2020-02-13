
tabla_de_numeros = []
numero_del_usuario = ""

while len(tabla_de_numeros) < 5:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = (input("Introduzca un número: "))
    tabla_de_numeros.append(numero_del_usuario)
    numero_del_usuario = ""
    print("Numero introducido.")

pequeno = tabla_de_numeros[0]
print("La tabla es esta: {}".format(tabla_de_numeros))

for numero in tabla_de_numeros:
    if numero < pequeno:
        print("El numero {} es menor que el {}".format(numero,pequeno))
        pequeno = numero

print("El numero mas pequeño es el {}".format(pequeno))