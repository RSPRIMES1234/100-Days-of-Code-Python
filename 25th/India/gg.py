import pandas as pd

df=pd.read_csv("gg2.csv")
print(df)
df.drop('Unnamed: 1', inplace=True, axis=1)
df.drop('Unnamed: 0', inplace=True, axis=1)
print(df)
df.to_csv("gg3.csv")