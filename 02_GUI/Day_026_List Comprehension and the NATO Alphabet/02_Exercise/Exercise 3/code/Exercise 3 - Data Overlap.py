with open("file1.txt") as file1_data:
    file1_list = list(file1_data.readlines())
    print(file1_list)
print("--------------------------------------------------------------")


with open("file2.txt") as file2_data:
    file2_list = list(file2_data.readlines())
    print(file2_list)
print("--------------------------------------------------------------")

result = [int(num) for num in file1_list if num in file2_list]


# Write your code above 👆

print(result)


