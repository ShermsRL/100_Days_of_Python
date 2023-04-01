# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         daily_temp = row[1]
# #         if daily_temp != "temp":
# #             temperatures.append(int(daily_temp))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print (data_dict)
#
#
# temp_list = data["temp"].to_list()
# print(data["temp"].max())
#
# print(data.condition)
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# temp_in_F = (monday.temp * 9/5) + 32
# print(temp_in_F)
#
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
#
# data_one = pandas.DataFrame(data_dict)
# data_one.to_csv("new_data.csv")

import pandas

gray_count = 0
cinnamon_count = 0
black_count = 0

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_color = squirrel_data["Primary Fur Color"]
for color in squirrel_color:
    if color == "Gray":
        gray_count += 1
    if color == "Black":
        black_count += 1
    if color == "Cinnamon":
        cinnamon_count += 1

squirrel_color_count = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_count, black_count, cinnamon_count]
}

data = pandas.DataFrame(squirrel_color_count)
data.to_csv("Squirrel color breakdown")
