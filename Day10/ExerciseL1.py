#                               💻 Exercises: Day 10

#                                 Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
print("\n--------- 1. For loop ----------\n")

count = 0
for i in range(11):
    print(i)

print("\n--------- 1.While Loop ----------\n")

while count < 11:
    print(count)
    count += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.

number = list(range(0, 11))
count = 10
number.reverse()
print("\n--------- 2. For loop ----------\n")

for num in number:
    print(num)

print("\n--------- 2. While loop ----------\n")

while count >= 0:
    print(count)
    count -= 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#       #
#       ##
#       ###
#       ####
#       #####
#       ######
#       #######
print("\n--------- Pattern ----------\n")

for i in range(8):
    for j in range(i+1):
        print("#", end="")
    print("\r")
print("\n--------- Pattern ----------\n")

# 4. Use nested loops to create the following:

#       # # # # # # # #
#       # # # # # # # #
#       # # # # # # # #
#       # # # # # # # #
#       # # # # # # # #
#       # # # # # # # #
#       # # # # # # # #
#       # # # # # # # #
print("\n--------- Pattern ----------\n")
for i in range(9):
    for j in range(9):
        print("# ", end="")
    print("\r")

# 5. Print the following pattern:

#       0 x 0 = 0
#       1 x 1 = 1
#       2 x 2 = 4
#       3 x 3 = 9
#       4 x 4 = 16
#       5 x 5 = 25
#       6 x 6 = 36
#       7 x 7 = 49
#       8 x 8 = 64
#       9 x 9 = 81
#       10 x 10 = 100
print("\n--------- Pattern ----------\n")
for i in range(11):
    for j in range(11):
        if (i == j):
            print(f'{i} x {j} = {i*j}', end="")
    print("\r")

print("\n---------  ----------\n")

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
types = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for type in types:
    print(type)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
print("\n--------- Even numbers ----------\n")
for number in range(101):
    if (number % 2 == 0):
        print(number)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
print("\n--------- odd numbers ----------\n")
for number in range(101):
    if (number % 2 != 0):
        print(number)
