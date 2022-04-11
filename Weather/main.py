

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



