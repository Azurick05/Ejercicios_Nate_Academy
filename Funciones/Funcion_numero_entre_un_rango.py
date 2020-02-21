"""
Ejercicio 20)
Escribe una funcion que dado un numero y un rango (otros dos numeros),
compruebe que ese numero está entre los dos (dentro del rango).
numero_en_rango(10, 1, 100) # Devuelve True
numero_en_rango(101, 1, 100) # Devuelve False
"""

low_range = int(input("Introduzca el primer numero del rango: "))
high_range = int(input("Introduzca el segundo numero del rango: "))

number = int(input("Introduzca el numero y le diré si está dentro del rango anterior: "))

def number_in_range (number, low_range, high_range):
    if number >= low_range and number <= high_range:
        return True
    else:
        return False

respuesta = number_in_range(number, low_range, high_range)
print(respuesta)