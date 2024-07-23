# import csv
#
# with open("weather_data.csv") as weth:
#     data=csv.reader(weth)
#     temps=[]
#     for _,value in enumerate(data):
#         if _ >0:
#             temps.append(int(value[1]))
#     print(temps)

import pandas as pd


color={}
color["Fur Color"]="Count"
df=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_count=df["Primary Fur Color"]
print(fur_count.count())
colors=["Gray","Cinnamon","Black"]
for _ in colors:
    gg = fur_count == f"{_}"

    count = gg.sum()
    color[f"{_}"] = count


df=pd.DataFrame(color)
# print(df["Primary Fur Color"])