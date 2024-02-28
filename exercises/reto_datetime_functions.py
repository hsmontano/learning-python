from datetime import date, datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
today = datetime.now()
vacancies_begin = parse(input("Indique la fecha en la que saldra de vacaciones (DD/MM/YYYY): "), dayfirst=True)
vacancies_fin = parse(input("Indique la fecha en la que regresara de vacaciones (DD/MM/YYYY): "), dayfirst=True)
day_of_vacancies = relativedelta(vacancies_begin,vacancies_fin)
day_for_vacancies = relativedelta(today,vacancies_begin)
print(f"Estara {abs(day_of_vacancies.days)} dias de vacaciones")
print(f"Faltan {abs(day_for_vacancies.months)} meses y {abs(day_for_vacancies.days)} dias para las vacaciones")