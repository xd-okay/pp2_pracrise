import datetime, calendar

now=datetime.datetime.now()
#1-2
#ago_5_days=past=now-datetime.timedelta(days=5)
# past=now-datetime.timedelta(days=1)
# tomorrow=datetime.datetime.date(now+datetime.timedelta(days=1))
# today=datetime.datetime.date(now)
# yesterday=datetime.datetime.date(past)

# print(yesterday)
# print(tomorrow)
# print(today)
#3
# clean=now.replace(microsecond=0)
# print(clean)

#4
now = datetime.datetime.now()
past_date = datetime.datetime(2023, 10, 1, 12, 0, 0) # Год, месяц, день, час, минута, секунда

difference = now - past_date

seconds_diff = difference.total_seconds()

print(f"Первая дата: {now}")
print(f"Вторая дата: {past_date}")
print(f"Разница в секундах: {seconds_diff}")