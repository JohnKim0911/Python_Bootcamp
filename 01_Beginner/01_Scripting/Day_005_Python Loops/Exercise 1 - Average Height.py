student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum = 0
count = 0

for i in student_heights:
    sum += i
    count += 1

result = round(sum / count)
print(result)

# ---------------- Result ---------------- #
# Input a list of student heights: 156 178 165 171 187
# 171
