#                               💻 Exercises: Day 14

# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#                                Exercises: Level 1

# 1. Explain the difference between map, filter, and reduce.
# The map() function is a built-in function that takes a function and iterable as parameters.
# The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.
# The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value.

# 2. Explain the difference between higher order function, closure and decorator
# higher order function : A function can take one or more functions as parameters, returned as a result of another function, modified, assigned to a variable
# closure : Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure.
# Decorator :   A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.


# 3. Define a call function before map, filter or reduce, see examples.

def square(x):
    return x ** 2


# square(numbers)
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# 4. Use for loop to print each country in the countries list.
for country in countries:
    print(country)

# 5. Use for to print each name in the names list.
for name in names:
    print(name)

# 6. Use for to print each number in the numbers list.
for number in numbers:
    print(number)
