#                               Exercises: Level 2

from countryList import countries as countries_list
from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Use map to create a new list by changing each country to uppercase in the countries list


def upper_case(x):
    return x.upper()


print(list(map(upper_case, countries)))

# 2. Use map to create a new list by changing each number to its square in the numbers list

print(list(map(lambda x: x**2, numbers)))

# 3. Use map to change each name to uppercase in the names list
print(list(map(upper_case, names)))

# 4. Use filter to filter out countries containing 'land'.


def country_contain_land(x):
    if 'land' in x:
        return True
    else:
        return False


print(list(filter(country_contain_land, countries)))

# 5. Use filter to filter out countries having exactly six characters.

print(list(filter(lambda x: len(x) == 6, countries)))

# 6. Use filter to filter out countries containing six letters and more in the country list.

print(list(filter(lambda x: len(x) >= 6, countries)))

# 7. Use filter to filter out countries starting with an 'E'

names = ""


def country_startswith_e(x):
    if x.startswith("E"):
        return True
    else:
        return False


print(list(filter(country_startswith_e, countries)))

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

#                               NOT POSSIBLE
a = map(lambda x: x**2, numbers)
b = filter(lambda x: x % 2 == 0, a)
c = reduce(lambda x, y: x+y, b)
print(c)

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

mixed_list = ["1", 2, 3, 4, "five", True]


# def get_string_lists(lst):
#     if type(lst) == str:
#         return True
#     else:
#         return False


# print(list(filter(get_string_lists, mixed_list)))


def get_string_lists():
    def get_string(lst):
        _list = filter(lambda x: type(x) == str, lst)
        return list(_list)
    return get_string


closure_result = get_string_lists()
print(closure_result(mixed_list))

# 10. Use reduce to sum all the numbers in the numbers list.

print((reduce(lambda x, y: x+y, numbers)))

# 11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

print(reduce((lambda x, y: f'{x}, {y}'), countries),
      "are north European countries")

# 12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).


def categorize_countries():
    def add(pattern):
        _list = filter(lambda x: pattern in x, countries_list)
        return list(_list)
    return add


closure_result = categorize_countries()
print(closure_result("dia"))

# 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.


def categorize_countries():
    def keys():
        count_list = {}
        for country in countries_list:
            key = country[0]
            values = filter(lambda x: x.startswith(key), countries_list)
            count_list[key] = len(list(values))
        return count_list
    return keys


new_dict = categorize_countries()
print(new_dict())

# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.


def get_first_ten_countries():
    return countries_list[0:10]


print(get_first_ten_countries())
# 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.


def get_last_ten_countries():
    countries_list.reverse()
    return countries_list[0:10]
    # return countries_list[len(countries_list)-11:len(countries_list)]


print(get_last_ten_countries())
