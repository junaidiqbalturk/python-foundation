#Dates in Python
#How to Format Dates in Python
from datetime import datetime
from datetime import date

now = (datetime.now())
print(now)

#strftime function format the date and time
print(now.strftime("%d/%m/%Y %H: %M: %S"))

#In order to print the date like 13-December-2020
print(now.strftime("%d/%B/%Y %H: %M: %S"))

#In order to print the date like 12-Dec-2020
print(now.strftime("%d/%b/%Y %H: %M: %S"))

# print(datetime.now().year)
# print(date.today())
# print(datetime.now().time())