# Calculates the sum of all the even numbers from 1 to 100.
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# ----------------------------- Result ---------------------------- #
# 2550
