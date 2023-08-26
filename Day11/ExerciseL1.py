#                                   💻 Exercises: Day 11

#                                     Exercises: Level 1

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num_1, num_2):
    return num_1 + num_2


print("Sum :", add_two_numbers(1, 2))

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.


def area_of_circle(radius):
    pi = 3.14
    return pi * radius * radius


print("Area of circle :", area_of_circle(10))

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.


def add_all_nums(*nums):
    total = 0
    for num in nums:
        if (type(num) == int):
            total += num
        else:
            return "Any of argment is not number"
    return total


print("add_all_nums : ", add_all_nums(1, 2, 2, 2, 2))

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.


def convert_celsius_to_fahrenheit(degree):
    fahrenheit = (degree * 9/5) + 32
    return f'{int(fahrenheit)}°F'


print("Celsius to fahrenheit : ", convert_celsius_to_fahrenheit(50))

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.


def check_season(month):
    season = ""
    month = str(month).capitalize()
    if month == "September" or month == "October" or month == "November":
        season = "Autumn"
    elif month == "December" or month == "January" or month == "February":
        season = "Winter"
    elif month == "March" or month == "April" or month == "May":
        season = "Spring"
    elif month == "June" or month == "July" or month == "August":
        season = "Summer"
    return season


print("Season :", check_season("june"))

# 6. Write a function called calculate_slope which return the slope of a linear equation


def calculate_slope(x1, y1, x2, y2):
    m = ((y2 - y1) / (x2 - x1))
    return m


print("slope of a linear equation :", calculate_slope(2, 8, 4, 10))

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.


def solve_quadratic_eqn(a, b, c):
    print(f'{a}x² + {b}x + {c} = 0')
    x1 = (-b + (b*b - 4*a*c) ** 0.5)/(2*a)
    x2 = (-b - (b*b - 4*a*c) ** 0.5)/(2*a)
    return f'x = {x1} or x = {x2}'


print(solve_quadratic_eqn(2, -5, -3))

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.


def print_list(list):
    print("element of the list :")
    for item in list:
        print(item, end=" ")
    print("\r")


print_list(["item1", "item2", "item3"])

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
#       print(reverse_list([1, 2, 3, 4, 5]))
#           # [5, 4, 3, 2, 1]
#       print(reverse_list1(["A", "B", "C"]))
#           # ["C", "B", "A"]


def reverse_list(list):
    count = len(list)-1
    new_list = []
    while count >= 0:
        new_list.append(list[count])
        count -= 1
    return new_list


print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items


def capitalize_list_items(list):
    for item in range(len(list)):
        list[item] = list[item].capitalize()
    return list


print(capitalize_list_items(["item1", "item2", "item3"]))

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
#       food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
#       print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
#       numbers = [2, 3, 7, 9];
#       print(add_item(numbers, 5))      [2, 3, 7, 9, 5]


def add_item(list, item):
    list.append(item)
    return list


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
#       food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
#       print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
#       numbers = [2, 3, 7, 9];
#       print(remove_item(numbers, 3))  # [2, 7, 9]


def remove_item(list, item):
    list.remove(item)
    return list


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
#       print(sum_of_numbers(5))  # 15
#       print(sum_all_numbers(10)) # 55
#       print(sum_all_numbers(100)) # 5050


def sum_of_numbers(num):
    sum_of_num = 0
    for i in range(num+1):
        sum_of_num += i
    return sum_of_num


print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.


def sum_of_odds(num):
    sum_of_num = 0
    for i in range(num+1):
        if i % 2 != 0:
            sum_of_num += i
    return sum_of_num


print(sum_of_odds(10))
# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.


def sum_of_even(num):
    sum_of_num = 0
    for i in range(num+1):
        if i % 2 == 0:
            sum_of_num += i
    return sum_of_num


print(sum_of_even(10))
