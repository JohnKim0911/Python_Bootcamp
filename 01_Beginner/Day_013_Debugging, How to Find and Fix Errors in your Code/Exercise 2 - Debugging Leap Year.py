year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# -------------- RESULT 1 --------------- #
# Which year do you want to check? 2024
# Leap year.

# -------------- RESULT 2 --------------- #
# Which year do you want to check? 2022
# Not leap year.

# -------------- REFERENCE --------------- #
# leap years in the first half of the 21st century:
# 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, and 2048
