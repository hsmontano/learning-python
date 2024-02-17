""" Escribe un programa en Python que dada una criptomoneda, la cantidad acumulada y 
    su correspondiente cotización por dólar del día, le permita al usuario conocer 
    la fecha completa y hora del momento en que obtuvo el sistema esa información, 
    así como el monto en US$ que tiene el usuario en su billetera digital. 
    Considerando un crecimiento del 5% por día, muéstrale al usuario para ese mismo día
    de la siguiente semana cuál sería su ganancia en US$. """
from datetime import datetime, timedelta
add_days = 8
percentage = 0.05
cryptomoney = input("Input type the cryptomoney name, please: ")
quantity_accumulated = int(input("Input type the quantity accumulated, please: "))
quotation = float(input("Input type the quotation per dollar of the day, please: "))

dt = datetime.now()
dt_formatted = dt.strftime("%A, %d of %B of %Y at the %I:%M:%Sp")
revenue_day = dt + timedelta(days=7)

print("The data was receive at: ", dt_formatted)
current_amount = quantity_accumulated * quotation
revenue = current_amount * percentage * add_days
sum_accu = 0
for x in range(0,8):
    sum_accu += current_amount * percentage
    print(sum_accu)

print(f"Your revenue for the next week is: {revenue} date {revenue_day.strftime("%A, %d of %B of %Y at the %I:%M:%Sp")}")
