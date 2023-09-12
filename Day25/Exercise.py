#                                   Exercises: Day 25
import pandas as pd

# 1. Read the hacker_news.csv file from data directory
csv_file = pd.read_csv("./Data/hacker_news.csv")
print(csv_file)

# 2. Get the first five rows
print("The first five rows : \n", csv_file.head())

# 3. Get the last five rows
print("The last five rows : \n", csv_file.tail())

# 4. Get the title column as pandas series
print(csv_file.columns)

# 5. Count the number of rows and columns
print(csv_file.shape)
#      - Filter the titles which contain python
print(csv_file[csv_file["title"].str.contains("python")])

#      - Filter the titles which contain JavaScript
print(csv_file[csv_file["title"].str.contains("JavaScript")])

#      - Explore the data and make sense of it
