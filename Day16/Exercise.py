#                              💻 Exercises: Day 16

from datetime import datetime, time, date

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print("current day", now.day)
print("current month", now.month)
print("current year", now.year)
print("current hour", now.hour)
print("current minute", now.minute)
print("current timestamp", now.timestamp())

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print("Current date", now.strftime("%m/%d/%Y, %H:%M:%S"))

# 3. Today is 5 December, 2019. Change this time string to time.
today = "5 December, 2019"
string_to_time = datetime.strptime(today, "%d %B, %Y")
print("string_to_time", string_to_time)

# 4. Calculate the time difference between now and new year.
now = datetime(now.year, now.month, now.day,
               now.hour, now.minute, now.second)
new_year = datetime(2024, 1, 1)
print('Time left for new year: ', new_year - now)

# 5. Calculate the time difference between 1 January 1970 and now.

date_1 = date(1970, 1, 1)
date_2 = date(2023, 9, 3)

print("the time difference between 1 January 1970 and now :", date_2 - date_1)

# 6. Think, what can you use the datetime module for? Examples:
#    - Time series analysis
#    - To get a timestamp of any activities in an application
#    - Adding posts on a blog
