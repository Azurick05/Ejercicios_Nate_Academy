
number_to_guess = int(input("Numero a adivinar del 0 al 10 (que tu comapañero no lo vea): "))

insert_number = 100
contador = 0

while number_to_guess != insert_number:
    insert_number = int(input("Adivine el numero del 0 al 10: "))
    contador += 1
    if insert_number != number_to_guess:
        print("Ha fallado, debe intentarlo de nuevo")

print("Lo has adivinado y el numero de intentos ha sido: {}".format(contador))