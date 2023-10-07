#                               Exercises: Level 3

# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
from countryData import countries_list
# Sort countries by name, by capital, by population
sort_by_name = sorted(countries_list, key=lambda x: x["name"])
print(sort_by_name)

sort_by_capital = sorted(countries_list, key=lambda x: x["capital"])
print(sort_by_capital)

sort_by_population = sorted(countries_list, key=lambda x: x["population"])
print(sort_by_population)

# Sort out the ten most spoken languages by location.
languages = []
for country in countries_list:
    languages.extend(country["languages"])

top_most_spoken_languages = [(i, languages.count(i)) for i in set(languages)]
print(sorted(top_most_spoken_languages,
      key=lambda x: x[1], reverse=True)[0:10])

# Sort out the ten most populated countries.
sort_by_population = sorted(
    countries_list, key=lambda x: x["population"], reverse=True)[0:10]
print(sort_by_population)
