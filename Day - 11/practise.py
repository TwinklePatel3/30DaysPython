# Declaring and Calling a Function
def generate_name():
    first_name = "Asabeneh"
    last_name = "Yetayeh"
    space = " "
    full_name = first_name + space + last_name
    print(full_name)


generate_name()

# Function Returning a Value - Part 1


def generate_name():
    first_name = "Asabeneh"
    last_name = "Yetayeh"
    space = " "
    full_name = first_name + space + last_name
    return full_name


print(generate_name())

# Function with Parameters


def add_ten(num):
    ten = 10
    return num + ten


print(add_ten(22))


def sum_of_two_number(num1, num2):
    return num1 + num2


print(sum_of_two_number(8, 9))
print(sum_of_two_number(num2=8, num1=9))


def greetings(name='Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message


print(greetings())
print(greetings('Asabeneh'))


def generate_full_name(first_name='Asabeneh', last_name='Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())
print(generate_full_name('David', 'Smith'))


def calculate_age(birth_year, current_year=2021):
    age = current_year - birth_year
    return age


print('Age: ', calculate_age(1821))


def weight_of_object(mass, gravity=9.81):
    # the value has to be changed to string first
    weight = str(mass * gravity) + ' N'
    return weight


# 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100))
print('Weight of an object in Newtons: ', weight_of_object(
    100, 1.62))  # gravity on the surface of the Moon

# Arbitrary Number of Arguments


def total_sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(total_sum(1, 2, 3, 4, 5))

# Default and Arbitrary Number of Parameters in Functions


def generate_groups(team, *args):
    print("team", team)
    for i in args:
        print(i)


print(generate_groups('Team-1', 'Asabeneh', 'Brook', 'David', 'Eyob'))

# You can pass functions around as parameters


def square_number(n):
    return n ** n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))
