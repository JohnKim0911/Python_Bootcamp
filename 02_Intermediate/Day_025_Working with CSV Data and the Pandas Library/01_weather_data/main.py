# ------------------ Using just file methods ------------------ #
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
# ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n',
#  'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']


# ------------------ Using csv library ------------------ #
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    # print(data)
    # ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n',
    # 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']
    # <_csv.reader object at 0x00000241B6216800>
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)  # [12, 14, 15, 14, 21, 22, 24]


# ------------------ Using the pandas library ------------------ #
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))  # <class 'pandas.core.frame.DataFrame'>
print(type(data["temp"]))  # <class 'pandas.core.series.Series'>

data_dict = data.to_dict()
print(data_dict)
# {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
#  'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
#  'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

temp_list = data["temp"].to_list()
print(temp_list)  # [12, 14, 15, 14, 21, 22, 24]
print(len(temp_list))  # 7

print(data["temp"].mean())  # 17.428571428571427
print(data["temp"].max())  # 24


# Get Data in Columns
print(data["condition"])
# 0     Sunny
# 1      Rain
# 2      Rain
# 3    Cloudy
# 4     Sunny
# 5     Sunny
# 6     Sunny
# Name: condition, dtype: object
print(data.condition)
# 0     Sunny
# 1      Rain
# 2      Rain
# 3    Cloudy
# 4     Sunny
# 5     Sunny
# 6     Sunny
# Name: condition, dtype: object


# Get Data in Row
print(data[data.day == "Monday"])
#       day  temp condition
# 0  Monday    12     Sunny

print(data[data.temp == data.temp.max()])
#       day  temp condition
# 6  Sunday    24     Sunny


# Get Row data value
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)  # 53.6
