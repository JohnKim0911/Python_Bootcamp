import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number_of_names = len(names) - 1
random_number = random.randint(0, number_of_names)
print(f"{names[random_number]} is going to buy the meal today!")


# --------------------------- Result ------------------------ #
# Give me everybody's names, separated by a comma. John, Angela, Tom, Harry
# Harry is going to buy the meal today!
