#                               Exercises: Level 3

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(list):
    from random import randint, shuffle
    # shuffle(list)
    print("original list :", list)

    n = len(list)
    for i in range(n):
        j = randint(0, n-1)
        element = list.pop(j)
        list.append(element)
    return list


print(shuffle_list([2, 3, 4, 5, 6]))

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.


def random_numbers():
    import random
    numbers = []
    # numbers = random.sample(range(0, 9), 7)
    tmp = random.randint(0, 9)

    for x in range(7):
        while tmp in numbers:
            tmp = random.randint(0, 9)
        numbers.append(tmp)
    return numbers


print(random_numbers())
