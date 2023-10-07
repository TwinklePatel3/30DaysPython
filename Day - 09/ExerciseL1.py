#                       💻 Exercises: Day 9

#                         Exercises: Level 1

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#          Enter your age: 30
#          You are old enough to learn to drive.
#          Output:
#          Enter your age: 15
#          You need 3 more years to learn to drive.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print(f'You need {18-age} more years to learn to drive.')

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
#       Enter your age: 30
#       You are 5 years older than me.

my_age = 20
your_age = int(input("Enter your age :"))
if my_age > your_age:
    age_diff = my_age - your_age
    print(f'You are {age_diff} years younger than me') if age_diff > 1 else print(
        f'You are {age_diff} year younger than me')
elif my_age < your_age:
    age_diff = your_age - my_age
    print(f'You are {age_diff} years older than me') if age_diff > 1 else print(
        f'You are {age_diff} year older than me')
else:
    print("We are same bro.")

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
#       Enter number one: 4
#       Enter number two: 3
#       4 is greater than 3

num_one = int(input("Enter number one: "))
num_two = int(input("Enter number two: "))

if num_one > num_two:
    print(f'{num_one} is greater than {num_two}')
elif num_one < num_two:
    print(f'{num_one} is smaller than {num_two}')
else:
    print(f'{num_one} is equal to {num_two}')
