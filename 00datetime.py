import datetime


birthday = datetime.date(2021, 11, 1)
today = datetime.date.today()
tdelta_day = datetime.timedelta(days = 7)
now = datetime.now()


till_birthday = today - birthday
print(till_birthday.days)
print(till_birthday.total_seconds())



print(today)
print(today.month)
print(today.day)
print(today.year)
print(today.weekday())
print(today.isoweekday())

print()

print(tdelta_day)

# tdelta_hour = datetime.timedelta(month = 3)
# print(tdelta_hour)




