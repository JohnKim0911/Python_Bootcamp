with open("file1.txt") as file1_data:
    file1_list = list(file1_data.readlines())
    print(file1_list)
    # ['3\n', '6\n', '5\n', '8\n', '33\n', '12\n', '7\n', '4\n', '72\n', '2\n', '42\n', '13\n']


with open("file2.txt") as file2_data:
    file2_list = list(file2_data.readlines())
    print(file2_list)
    # ['3\n', '6\n', '13\n', '5\n', '7\n', '89\n', '12\n', '3\n', '33\n', '34\n', '1\n', '344\n', '42\n']


result = [int(num) for num in file1_list if num in file2_list]
print(result)  # [3, 6, 5, 33, 12, 7, 42, 13]



