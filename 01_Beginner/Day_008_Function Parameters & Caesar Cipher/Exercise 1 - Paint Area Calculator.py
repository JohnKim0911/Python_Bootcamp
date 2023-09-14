import math


def paint_calc(height, width, cover):
    cal_result = (height * width) / cover
    # print(cal_result)
    can_needed = math.ceil(cal_result)
    print(f"You'll need {can_needed} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5  # 1 can of paint can cover 5 square meters of wall.
paint_calc(height=test_h, width=test_w, cover=coverage)


# ------------------------------------ Result -------------------------------------- #
# Height of wall: 3
# Width of wall: 9
# You'll need 6 cans of paint.
