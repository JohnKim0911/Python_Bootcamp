# 1 can of paint can cover 5 square meters of wall.

# Write your code below this line 👇
import math


def paint_calc(height, width, cover):
    cal_result = (height * width) / cover
    # print(cal_result)
    can_needed = math.ceil(cal_result)
    print(f"You'll need {can_needed} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
