#                               Exercises: Day 20
import json
import pandas as pd
from statistics import *
import requests

# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
romeo_and_juliet_url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(romeo_and_juliet_url)
words = response.text.split()
most_frequent_words = [(words.count(x), x) for x in set(words)]
print("The 10 most frequent words : ", sorted(
    most_frequent_words, reverse=True)[:10])

# 2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
#   -   the min, max, mean, median, standard deviation of cats' weight in metric units.
#   -   the min, max, mean, median, standard deviation of cats' lifespan in years.
#   -   Create a frequency table of country and breed of cats

cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
cats_details = response.json()
weight_metric = [int(x["weight"]['metric'].split(
    "-")[1]) - int(x["weight"]['metric'].split("-")[0])for x in cats_details]

lifespan = [int(x['life_span'].split(
    "-")[1]) - int(x['life_span'].split("-")[0])for x in cats_details]
country = [{"country": x["origin"], "breed":x["name"]} for x in cats_details]

print(f"The min = {min(weight_metric)}, max = {max(weight_metric)}, mean = {mean(weight_metric)}, median = {median(weight_metric)}, standard deviation = {stdev(weight_metric)} of cat's weight in metric units.")
print(f"The min = {min(lifespan)}, max = {max(lifespan)}, mean = {mean(lifespan)}, median = {median(lifespan)}, standard deviation = {stdev(lifespan)} of cat's lifespan in yearss.")

df = pd.DataFrame(country)
print("\nFrequency Table for the Grade in the dataset : ")
ft = pd.crosstab(index=df['country'], columns=df['breed'])
print(ft)

# 3. Read the countries API and find
#   -   the 10 largest countries
#   -   the 10 most spoken languages
#   -   the total number of languages in the countries API

country_url = "https://restcountries.com/v3.1/all"
response = requests.get(country_url)
# countris = response.json()
countries = json.loads(response.text)

country = [{"country": x["name"]["common"], "area":x['area']}
           for x in countries]

print("The 10 largest countries :", sorted(
    country, key=lambda x: x["area"], reverse=True)[:10])
language_list = []

for data in countries:
    for key, value in data.items():
        if key == "languages":
            language_list.append(list(value.values()))

flatten_language_list = [x for row in language_list for x in row]
most_spoken_language = [(flatten_language_list.count(x), x)
                        for x in set(flatten_language_list)]
print(sorted(most_spoken_language, key=lambda x: x[0], reverse=True)[:10])
print("total number of languages in the countries API :",
      len(set(flatten_language_list)))
# UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
