print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_combined = name1 + name2
name_lower = name_combined.lower()

true_count = 0
true_count += name_lower.count("t")
true_count += name_lower.count("r")
true_count += name_lower.count("u")
true_count += name_lower.count("e")
true_count *= 10

love_count = 0
love_count += name_lower.count("l")
love_count += name_lower.count("o")
love_count += name_lower.count("v")
love_count += name_lower.count("e")

point = true_count + love_count

if point < 10 or point > 90:
    print(f"Your score is {point}, you go together like coke and mentos.")
elif point >= 40 and point <= 50:
    print(f"Your score is {point}, you are alright together.")
else:
    print(f"Your score is {point}.")


# ------------------------------------ Result --------------------------------- #
# Welcome to the Love Calculator!
# What is your name?
# Brad Pitt
# What is their name?
# Jennifer Aniston
# Your score is 73.
