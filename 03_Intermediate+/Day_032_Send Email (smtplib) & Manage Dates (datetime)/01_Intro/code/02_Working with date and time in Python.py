# Working with date and time in Python
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

print(f"- now: {now}")
print(f"- year: {year}")
print(f"- month: {month}")
print(f"- day_of_week: {day_of_week}\n")

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(f"- date_of_birth: {date_of_birth}")


# ---------------------- Result ------------------------ #
# - now: 2023-08-30 20:36:41.969886
# - year: 2023
# - month: 8
# - day_of_week: 2
#
# - date_of_birth: 1995-12-15 04:00:00
