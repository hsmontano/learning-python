""" in this lesson we going to see the predefined modules """
""" the first one that we will do is import the date function of datatime module """
from datetime import date, datetime
""" then, we instance the today function """
d = date.today()
print("This is a date without format --> ", d)

d_formatted = d.strftime("%d/%m/%y")
print("This is a date with simple format --> ", d_formatted)

d_formatted = d.strftime("%d/%m/%Y")
print("This is a date with simple format 4 numbers of the year --> ", d_formatted)

dt = datetime.now()
dt_formatted = dt.strftime("%A %d/%m/%y %H:%M:%S")
print("This is a datetime with format dd/mm/aa hh:mm:ss: --> ", dt_formatted)

dt_formatted = dt.strftime("%A %d/%m/%y %I:%M:%S")
print("This is a datetime with format dd/mm/aa hh:mm:ss: --> ", dt_formatted)
