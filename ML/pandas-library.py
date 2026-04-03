# Pandas Library is used for creating DataFrames and to work with excel files(CSV - Comma Seperated Values) and Data Analysis

# importing pandas library with alias pd
import pandas as pd

# DataFrame()
data = {"Name": ["A", "B", "C", "D"], "Age": [20, 30, 40, 50]}
df = pd.DataFrame(data)
print(df)

# From List of Dictionaries
df = pd.DataFrame([
    {"Name": "Akshay", "Age": 24},
    {"Name": "Ajay", "Age": 23},
    {"Name": "Jay", "Age": 35},
])
print(df)

# read_csv()
df = pd.read_csv("data.csv")
print(df.head())
# info()
print(df.info())

df = pd.read_csv("weather.csv")
print(df)
print(df.head())
print(df.info())
print(df.columns)

# head() and tail()
# To fetch the data from top or bottom with number-of-data
print(df.head(2))
print(df.tail(2))

# Targetting individual columns
# Column based selection
print("Cities:")
print(df["city"])
print("Temperature")
print(df["temp"])

# loc - label-based selection
# Row based selction
print(df.loc[3])

# iloc - index-based selection
print(df.iloc[0:1])

# conditional filtering
print(df[df["temp"] > 35.5])

print(df[(df["humidity"] > 40) & (df["humidity"] < 50)])

#new column
df["average-rainfall"]=[20,23.5,15.5,12.5,29,39]
print(df)

#update column
df["humidity"]=df["humidity"]+1
print(df)

#isnull()
print(df.isnull())

#dropna()
#df.dropna(inplace=True)
#print(df)

#fillna()
df.fillna(0, inplace=True)
print(df)

#describe()
print(df.describe())

#mean()
print(df["humidity"].mean())

#median()
print(df["humidity"].median())

#mode()
print(df["humidity"].mode())

#sort_values()
print(df.sort_values(by="temp"))

#groupby
data={
    "Dept":["HR","IT","HR","IT"],
    "Salary":[20000,30000,40000,50000],
}
df=pd.DataFrame(data)
print(df)
print(df.groupby("Dept").sum())

#unique()
print(df["Dept"].unique())

#value_counts()
print(df["Dept"].value_counts())

#df.to_csv("output.csv", index=False)
df.to_csv("output.csv", index=False)
print(df)