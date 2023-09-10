# For Loop
numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)  # [2, 3, 4]


# List Comprehension
new_list = [n + 1 for n in numbers]
print(new_list)  # [2, 3, 4]


# String as List
name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)  # ['A', 'n', 'g', 'e', 'l', 'a']


# Range as List
range_list = [n * 2 for n in range(1, 5)]
print(range_list)  # [2, 4, 6, 8]


# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)  # ['Alex', 'Beth', 'Dave']

upper_case_names = [name.upper() for name in names if len(name) > 4]
print(upper_case_names)  # ['CAROLINE', 'ELANOR', 'FREDDIE']


# Dictionary Comprehension
import random

student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)  # {'Alex': 95, 'Beth': 74, 'Caroline': 63, 'Dave': 35, 'Elanor': 94, 'Freddie': 56}

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)  # {'Alex': 95, 'Beth': 74, 'Caroline': 63, 'Elanor': 94}
