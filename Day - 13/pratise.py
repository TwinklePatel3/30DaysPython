# List Comprehension
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

lst = [i for i in language]
print(type(lst))
print(lst)

numbers = [i for i in range(0, 10)]
print(numbers)

sqr = [i*i for i in range(1, 5)]
print(sqr)

numbers = [(i, i*i) for i in range(0, 10)]
print(numbers)

even_numbers = [i for i in range(0, 10) if i % 2 == 0]
print(even_numbers)

odd_numbers = [i for i in range(0, 10) if i % 2 != 0]
print(odd_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [number for row in list_of_lists for number in row]
print(flat_list)


# lambda
def add_two_nums(x, y): return x+y


print(add_two_nums(1, 2))
print((lambda a, b: a+b)(2, 3))


def square(a): return a**2


print(square(3))


# Multiple variables
def multiple_variable(a, b, c): return a ** 2 - 3 * b + 4 * c


print(multiple_variable(5, 5, 3))  # 22


def power(x):
    return lambda a: x**a


cube = power(2)(2)
print(cube)
