from datetime import date, datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

fecha = date.today()
fecha_hora = datetime.now()
print("Date formats")
print("Date:",fecha)
print("Date and Time:",fecha_hora)
print("Date and Time (ctime format):", fecha_hora)
print("Date format one:",fecha_hora.strftime("%d/%m/%y"))
print("Date format two:",fecha_hora.strftime("%d/%m/%y %H:%M:%S"))
print("Date format three:",fecha_hora.strftime("%A %d/%m/%y %I:%M:%S%p"))
print("Calculate with Date")
today=datetime.now()
birthdate= parse(input("Input birthdate (DD/MM/YYYY): "), dayfirst=True)
age= relativedelta(today,birthdate) 
print(f"You have {age.years} years old, {age.months} months and {age.days} days")
oldnight_days = today - today.replace(day=31, month=12)
chrismas_day= today-today.replace(day=24,month=12)
print(f"left {abs(chrismas_day.days)} for the chrismas")
print(f"left {abs(oldnight_days.days)} for the end of year")
