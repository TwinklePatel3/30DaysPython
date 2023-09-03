from math import pow
import math

#                               SyntaxError

# print 'hello world' # Generate error
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?


print("Hello World")  # fixed by using parentheses

#                               NameError

# print(msg) # Generate error
# NameError: name 'msg' is not defined

msg = "Welcome"  # fixed error by defining name/variable
print(msg)


#                              IndexError

numbers = [1, 2, 3, 4, 5]
# print(numbers[5]) # Generate error
# IndexError: list index out of range ,because the list has only indexes from 0 to 4 , so it was out of range.

print(numbers[3])  # fixed

#                              ModuleNotFoundError

# import maths # Generate error
# ModuleNotFoundError: No module named 'maths'
# import math #fixed


#                               AttributeError
# print(math.PI)   # Generate error
# AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)


#                              KeyError
users = {'name': 'Asab', 'age': 250, 'country': 'Finland'}
print(users['name'])
# print(users['county'])  # Generate error
# KeyError: 'county'
print(users['country'])  # fixed


#                              TypeError

# print(2+"2")  # Generate error
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(2+int("2"))

#                               ImportError

# # from math import power  # Generate error
# ImportError: cannot import name 'power' from 'math' (/usr/local/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload/math.cpython-311-darwin.so)

# from math import pow # fixed
print(pow(2, 2))


#                              ValueError

# print(int('12a')) # Generate error
# ValueError: invalid literal for int() with base 10: '12a'
# In this case we cannot change the given string to a number, because of the 'a' letter in it.

#                               ZeroDivisionError

# print(1/0) # Generate error
# ZeroDivisionError: division by zero
# We cannot divide a number by zero.
