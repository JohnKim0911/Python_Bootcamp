# ------------- For Loop with Lists ------------------ #
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Apple
# Apple Pie
# Peach
# Peach Pie
# Pear
# Pear Pie


# ------------- For Loop with Range ------------------ #
for number in range(1, 100):
    print(number)  # 1 ~ 99


for number in range(1, 101):
    print(number)  # 1 ~ 100


for number in range(1, 11, 3):
    print(number)  # 1, 4, 7, 10


# ----- Calculating the sum of all the numbers from 1 to 100. ----- #
total = 0
for number in range(1, 101):
    total += number
print(total)  # 5050

