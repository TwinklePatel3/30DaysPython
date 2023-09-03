from datetime import time
from datetime import date
from datetime import datetime

print(dir(datetime))
now = datetime.now()
print(now)
print(now.day)
print(now.month)
print(now.year)

print(now.hour)
print(now.minute)
print(now.timestamp())
print(now.time())

new_year = datetime(2020, 1, 1)
print(new_year)
print(new_year.day)
print(new_year.month)
print(new_year.year)

print(now.strftime('%H:%M:%S'))
print(now.strftime("%m/%d/%Y, %H:%M:%S,%j,%c"))

d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month)  # 12
print("Current day:", today.day)
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
# Time left for new year: 26 days, 23: 01: 00
print('Time left for new year:', diff)
