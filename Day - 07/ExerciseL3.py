#                                   💻 Exercises: Level 3

# # sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)
print(ages_set)
print(max(len(ages_set), len(age)))  # lenght of age list is bigger

# 2. Explain the difference between the following data types: string, list, tuple and set
# String : Any data type written as text is a string. Any data under single, double or triple quote are strings.
# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
# Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
# Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sent = "I am a teacher and I love to inspire and teach people"
unique_words = set(sent.split(" "))
print("Total unique words : ", len(unique_words))
