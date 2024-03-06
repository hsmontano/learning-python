""" te solicitamos que escribas un programa en pseudocódigo que reciba cinco criptomonedas, 
    cada una con sus respectivas cantidades y precios en dólares americanos (USD), y luego imprima el valor total en USD que tienes acumulado. """ 
count = 0
total = 0
while count < 5:
    crypto_name = input("Type the cryptomoney name number: ")
    quantity = float(input("Type the quantity of cryptomoney: "))
    total += quantity
    count += 1

print(f"The amount total is: {total}")
