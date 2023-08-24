# Using just file methods
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
print("------------------------------------------------------")


# Using csv library
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
print("------------------------------------------------------")


# Using the pandas library
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))
print("------------------------------------------------------")

data_dict = data.to_dict()
print(data_dict)
print("------------------------------------------------------")

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))
print("------------------------------------------------------")

print(data["temp"].mean())
print(data["temp"].max())
print("------------------------------------------------------")

# Get Data in Columns
print(data["condition"])
print(data.condition)
print("------------------------------------------------------")

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
print("------------------------------------------------------")

# Get Row data value
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)
