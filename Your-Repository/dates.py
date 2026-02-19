import datetime, calendar

now=datetime.datetime.now()
date=datetime.datetime.date(now)
month=date.month
year=date.year
last_day = calendar.monthrange(year, month)[1]

print(date)
print(month)
print(year)
print(f"In {year}, {month} has {last_day} days")

