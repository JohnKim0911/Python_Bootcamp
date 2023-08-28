# Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "appbreweryinfo@gmail.com"   # Use your email
MY_PASSWORD = "abcd1234()"              # Use your password (Use app password instead)

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)

# ------ Reference for 'Day number' --------
# 1: Monday
# 2: Tuesday
# 3: Wednesday
# 4: Thursday
# 5: Friday
# 6: Saturday
# 7: Sunday
# ------------------------------------------

# if weekday == 1:   # For monday: Use this instead.
if weekday == 6:     # For Saturday: Use this.
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


############### The codes below are already included above. ##############

# ## Sending Email with Python
# import smtplib
#
# my_email = "appbreweryinfo@gmail.com"
# password = "abcd1234()"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="appbrewerytesting@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )


## Working with date and time in Python
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)
