# 💻 Exercises: Day 13

# 1. Filter only negative and zero in the list using list comprehension
#       numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
only_negative_zero = [i for i in numbers if i <= 0]
print(only_negative_zero)

# 2. Flatten the following list of lists of lists to a one dimensional list :
#       list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
#       output
#       [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = [
    number for row in list_of_lists for number in row for number in number]
print(flat_list)

# 3. Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

list_of_tuple = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(0, 11)]
# list_of_tuple = [tuple((i**j) for j in range(0, 6)) for i in range(0, 11)]
[i for si in range(0, 11) for i in range(0, 6)]

# 4. Flatten the following list to a new list:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_country_list = [[i[0].upper(), i[0][0:3].upper(), i[1].upper()]
                        for row in countries for i in row]
print(flatten_country_list)

# 5. Change the following list to a list of dictionaries:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
list_of_dictionaries = [{'country': i[0].upper(), 'city':i[1].upper()}
                        for row in countries for i in row]
print(list_of_dictionaries)

# 6.Change the following list of lists to a list of concatenated strings:
#  names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
list_of_concatenated_strings = [item[0] + " " + item[1]
                                for subitem in names for item in subitem]
print(list_of_concatenated_strings)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.


def slope(x1, y1, x2, y2): return (y2-y1/x2-x1)


print(slope(2, 3, 4, 8))

print((lambda x1, y1, x2, y2: (y2-y1/x2-x1))(2, 4, 8, 10))
