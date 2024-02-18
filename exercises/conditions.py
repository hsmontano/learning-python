""" Escribe un programa en pseudocódigo que dadas tres criptomonedas y sus respectivas cantidades, 
    imprima de forma ordenada decreciente cada moneda con sus respectivos valores. """

crypto_one = input("Type the cryptomoney name number one: ")
quantity_one = int(input("Type the quantity of cryptomoney: "))

crypto_two = input("Type the cryptomoney name number two: ")
quantity_two = int(input("Type the quantity of cryptomoney: "))

crypto_three = input("Type the cryptomoney name number three: ")
quantity_three = int(input("Type the quantity of cryptomoney: "))

if quantity_one > quantity_two and quantity_one > quantity_three:
    print(f"cryptomoney name is: {crypto_one} and its value is: {quantity_one}")
    if quantity_two > quantity_three:
        print(f"cryptomoney name is: {crypto_two} and its value is: {quantity_two}")
        print(f"cryptomoney name is: {crypto_three} and its value is: {quantity_three}")
    else:
        print(f"cryptomoney name is: {crypto_three} and its value is: {quantity_three}")
        print(f"cryptomoney name is: {crypto_two} and its value is: {quantity_two}")
elif quantity_two > quantity_one and quantity_two > quantity_three:
    print(f"cryptomoney name is: {crypto_two} and its value is: {quantity_two}")
    if quantity_one > quantity_three:
        print(f"cryptomoney name is: {crypto_one} and its value is: {quantity_one}")
        print(f"cryptomoney name is: {crypto_three} and its value is: {quantity_three}")
    else:
        print(f"cryptomoney name is: {crypto_three} and its value is: {quantity_three}")
        print(f"cryptomoney name is: {crypto_two} and its value is: {quantity_two}")
else:
    print(f"cryptomoney name is: {crypto_three} and its value is: {quantity_three}")
    if quantity_one > quantity_two:
        print(f"cryptomoney name is: {crypto_one} and its value is: {quantity_one}")
        print(f"cryptomoney name is: {crypto_two} and its value is: {quantity_two}")
    else:
        print(f"cryptomoney name is: {crypto_two} and its value is: {quantity_two}")
        print(f"cryptomoney name is: {crypto_one} and its value is: {quantity_one}")