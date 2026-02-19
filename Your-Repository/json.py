import json

import datetime

now=datetime.datetime.now()
date=datetime.datetime.date(now)
month=date.month
year=date.year
day=date.day

current_date={"day": day, "month": month, "year": year}
print(json.dumps(current_date)) 