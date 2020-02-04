
number_to_guess = int(input("Numero a adivinar del 0 al 10 (que tu comapañero no lo vea): "))

insert_number = 100

while number_to_guess != insert_number:
    insert_number = int(input("Adivine el numero del 0 al 10: "))

    if insert_number != number_to_guess:
        print("Ha fallado, debe intentarlo de nuevo")

print("Lo has adivinado!")