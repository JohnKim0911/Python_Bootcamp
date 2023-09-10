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
