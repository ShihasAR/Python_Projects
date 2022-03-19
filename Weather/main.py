# import csv
#
#
# temperature = []
# with open("weather_data.csv","r") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != "temp":
#          temperature.append(int(row[1]))
#
# print(temperature)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# # def avg (lst):
# #    return sum(lst)/len(lst)
# #
# #
# # data_list = round(avg(data["temp"].to_list()),3)
# # print(f"average is : {data_list}")
#
# monday = data[data.day == "Monday"]
# temperature = monday.temp
#
# temp_F = (temperature*1.8) + 32
# print(temp_F)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_sqrls = len(data[data["Primary Fur Color"] == "Gray"])
red_sqrls = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sqrls = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur" : ["Gray","Red","Black"],
    "Count" : [gray_sqrls,red_sqrls,black_sqrls]

}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels.csv")



