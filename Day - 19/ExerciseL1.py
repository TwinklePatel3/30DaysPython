#                                  💻 Exercises: Day 19

#                                    Exercises: Level 1

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
# a) Read obama_speech.txt file and count number of lines and words
# b) Read michelle_obama_speech.txt file and count number of lines and words
# c) Read donald_speech.txt file and count number of lines and words
# d) Read melina_trump_speech.txt file and count number of lines and words

import json
import re


def count_lines_and_words(file_path):
    with open(file_path) as f:
        file_read = f.read()
        lines = file_read.splitlines()
        words = len(file_read.split())
    print(
        f"There are {len(lines)} lines and {words} words in {file_path}")


count_lines_and_words('./Data/obama_speech.txt')
count_lines_and_words('./Data/michelle_obama_speech.txt')
count_lines_and_words('./Data/donald_speech.txt')
count_lines_and_words('./Data/melina_trump_speech.txt')

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 10))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic'),
# (24, 'Spanish'),
# (9, 'Russian'),
# (9, 'Portuguese'),
# (8, 'Dutch'),
# (7, 'German'),
# (5, 'Chinese'),
# (4, 'Swahili'),
# (4, 'Serbian')]
# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 3))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic')]


def most_spoken_languages(file_name, num):
    with open(file_name) as json_file:
        content = json_file.read()
        dct = json.loads(content)
        languages = []
        languages.extend(x for row in dct for x in row['languages'])
        most_spoken = [(languages.count(x), x) for x in languages]
    return sorted(set(most_spoken), reverse=True)[0:int(num)]


print(most_spoken_languages('./data/countries_data.json', 10))
print(most_spoken_languages('./data/countries_data.json', 3))

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
# # Your output should look like this
# print(most_populated_countries(filename='./data/countries_data.json', 10))
# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000},
# {'country': 'Indonesia', 'population': 258705000},
# {'country': 'Brazil', 'population': 206135893},
# {'country': 'Pakistan', 'population': 194125062},
# {'country': 'Nigeria', 'population': 186988000},
# {'country': 'Bangladesh', 'population': 161006790},
# {'country': 'Russian Federation', 'population': 146599183},
# {'country': 'Japan', 'population': 126960000}
# ]

# # Your output should look like this

# print(most_populated_countries(filename='./data/countries_data.json', 3))
# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000}
# ]


def most_populated_countries(filename, num):
    with open(filename) as json_file:
        content = json_file.read()
        dct = json.loads(content)
        country_population_wise = []
        country_population_wise.extend(
            {'country': x["name"], 'population': x["population"]} for x in dct)
    return sorted(country_population_wise, reverse=True, key=lambda x: x["population"])[0:int(num)]


print(most_populated_countries('./Data/countries_data.json', 10))
print(most_populated_countries('./Data/countries_data.json', 3))
