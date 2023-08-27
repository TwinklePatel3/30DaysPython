import math
from statistics import *
import os
from mymodule import genrate_full_name, sum_two_nums as total, person, gravity
print(genrate_full_name("Twinkle", "Patel "))
print(total(2, 3))
mass = 100
weight = mass * gravity
print("weight :", weight)
print(person)


# OS Module
# os.mkdir("main.py")
# os.chdir('main.py')
# print(os.getcwd())
# os.rmdir('/Users/apple/Desktop/30DaysPython/main.py')

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

print(math.pi)
print(math.sqrt(49))
print(math.pow(2, 3))
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))
