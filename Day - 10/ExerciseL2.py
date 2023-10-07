#                               Exercises: Level 2

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#               The sum of all numbers is 5050.
sum_of_all_numbers = 0
for number in range(0, 101):
    sum_of_all_numbers += number
print("sum of all numbers", sum_of_all_numbers)

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#       The sum of all evens is 2550. And the sum of all odds is 2500.
sum_of_all_evens = 0
sum_of_all_odds = 0

for number in range(101):
    if (number % 2 == 0):
        sum_of_all_evens += number
    else:
        sum_of_all_odds += number

print(
    f'The sum of all evens is {sum_of_all_evens}. And the sum of all odds is {sum_of_all_odds}.')
