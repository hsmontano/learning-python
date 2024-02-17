""" Escribe un programa en Python que dada una criptomoneda, 
    la cantidad acumulada y su correspondiente cotización por dólar del día, 
    le permita al usuario conocer la fecha completa y hora del momento 
    en que obtuvo el sistema esa información """
from datetime import datetime

crypto = input("type a cryptomoney name, please: ")
quantity_accu = int(input("type the quantity accumulated, please: "))
quotation = float(input("type its quotation for cryptomoney, please: "))
dt = datetime.now()
dt_formatted = dt.strftime("%A, %d of %B of %Y at the %H:%M:%S")
print(f'''
    cryptomomey name: {crypto}
    quatity accumulated: {quantity_accu}
    quotation for cryptomoney: {quotation}
''')
print("The data was receive at: ", dt_formatted)
