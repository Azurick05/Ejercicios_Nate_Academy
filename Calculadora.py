insertar_operacion = input("¿Que operacion quieres realizar? (A:multiplicar/ B:dividir / C:sumar / D:restar):").upper()

primer_numero = int(input("Introduzca el primer numero: "))
segundo_numero = int(input("Introduzca el segundo numero: "))

resultado = 0

if insertar_operacion == "A":
    resultado = primer_numero * segundo_numero
elif insertar_operacion == "B":
    resultado = primer_numero / segundo_numero
elif insertar_operacion == "C":
    resultado = primer_numero + segundo_numero
elif insertar_operacion == "D":
    resultado = primer_numero - segundo_numero

print("Resultado: {}".format(resultado))