# While Loop

count = 0

while count < 5:
    print(count)
    count += 1
else:
    print(count)

# Break and Continue - Part 1
count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break
else:
    print(count)


count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        count += 1
        continue
# else:
#     print(count)

# For Loop
numbers = [0, 1, 2, 3, 4, 5]

for number in numbers:
    print(number)

language = "python"

for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i], i)


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    # for short hand conditions need both if and else statements
    print('Next number should be ', number +
          1) if number != 5 else print("loop's end")
print('outside the loop')


for key in person:
    if key == "skills":
        for skill in person['skills']:
            print(skill)

# For else

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# pass
for number in range(6):
    pass
