from functools import reduce


def sum_num(nums):
    return sum(nums)


def higher_level_function(f, lst):
    total = f(lst)
    return total


print(higher_level_function(sum_num, [1, 2, 3, 4, 5]))


def sqaure(num):
    return num**2


def cube(num):
    return num**3


def absolute(num):
    if num >= 0:
        return num
    else:
        return -num


def higher_order_func(type):
    if type == "square":
        return sqaure
    elif type == "cube":
        return cube
    else:
        return absolute


result = higher_order_func('square')
print(result(3))       # 9
result = higher_order_func('cube')
print(result(3))       # 27
result = higher_order_func('absolute')
print(result(-3))


def add_ten():
    ten = 10

    def add(num):
        return num + ten
    return add


closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20


def upper_case_function(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper


def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


@split_string_decorator
@upper_case_function
def greeting():
    return "Welcome to python learn session."


print(greeting())


def decor_with_para(function):
    def wrapper_with_para(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_with_para


@decor_with_para
def print_fname(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))


print_fname("Asabeneh", "Yetayeh", 'Finland')


numbers = [1, 2, 3, 4, 5]
numbers_sqr = map(sqaure, numbers)
print(list(numbers_sqr))

print(list(map(lambda x: x ** 2, numbers)))
print(list(map(str, numbers)))


def even_num(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(list(filter(even_num, numbers)))


numbers_str = ['1', '2', '3', '4', '5']  # iterable


def add_two_nums(x, y):
    return int(x) + int(y)


total = reduce(add_two_nums, numbers_str)
print(total)    # 15
