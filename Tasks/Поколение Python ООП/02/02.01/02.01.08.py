# Каждый месяц в Сан-Диего организовывается встреча любителей Python, которая проходит в четвертый четверг месяца.
# Напишите программу, которая определяет день проведения очередной встречи питонистов в Сан-Диего.

from calendar import monthcalendar
from datetime import date

year, month = int(input()), int(input())
date_list = monthcalendar(year, month)
if date_list[0][3] != 0:
    day = date_list[3][3]
else:
    day = date_list[4][3]
print(date(year, month, day).strftime("%d.%m.%Y"))
