try:
    print(10+'10')
except:
    print("Something went wrong.")


try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

try:
    print(10+'10')
except Exception as e:
    print(e)


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
# TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
print(sum_of_five_nums(*lst))

for index, item in enumerate([20, 30, 40]):
    print(index, item)


countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

for index, i in enumerate(countries):
    if i == "Norway":
        print(f'found at index {index}')

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

fruits_and_veg = []

for f, v in zip(fruits, vegetables):
    fruits_and_veg.append({'fruits': f, 'veg': v})

print(fruits_and_veg)
