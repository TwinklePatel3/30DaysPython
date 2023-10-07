import pandas as pd  # importing pandas as pd
import numpy as np  # importing numpy as np
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)
s = pd.Series(nums, index=([1, 2, 3, 4, 5]))
print(s)

fruits = ["Apple", "Banana", "Chickoo"]
print(pd.Series(fruits, index=([1, 2, 3])))

person = {"name": "Twinkle", "country": "India", "city": "Mumbai"}
print(pd.Series(person))

s = pd.Series(10, index=([1, 2, 3, 4]))
print(s)

s = pd.Series(np.linspace(5, 10, 10))
print(s)


data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]

df = pd.DataFrame(data, columns=["Name", "Country", "City"])
print(df)

data = {'Name': ['Asabeneh', 'David', 'John'], 'Country': [
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}

print(pd.DataFrame(data))

data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]

s = pd.DataFrame(data)
print(s)

df = pd.read_csv("./Day25/weight-height.csv")
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)

heights = df['Height']
print(heights)

weights = df['Weight']  # this is now a series
print(weights)

print(len(heights) == len(weights))
print(heights.describe())  # give statisical information about height data
print(weights.describe())  # give statisical information about height data
print(df.describe())

data = [
    {"Name": "Asabeneh", "Country": "Finland", "City": "Helsinki"},
    {"Name": "David", "Country": "UK", "City": "London"},
    {"Name": "John", "Country": "Sweden", "City": "Stockholm"}]
df = pd.DataFrame(data)
print(df)
weights = [74, 78, 69]
df["Weight"] = weights
print(df)
heights = [173, 175, 169]
df['Height'] = heights
print(df)
df['Height'] = df['Height'] * 0.01
print(df)


def calculate_bmi():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w, h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi


bmi = calculate_bmi()
df['BMI'] = bmi
print(df)
df['BMI'] = round(df['BMI'], 1)
print(df)
birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2023, index=[0, 1, 2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)
print(df.Weight.dtype)
print(df['Birth Year'].dtype)
df["Birth Year"] = df["Birth Year"].astype(int)
print(df['Birth Year'].dtype)
df['Current Year'] = df['Current Year'].astype('int')
print(df['Current Year'].dtype)
ages = df['Current Year'] - df['Birth Year']
print(ages)
df["Ages"] = ages
print(df)
print(df[df['Ages'] < 120])
