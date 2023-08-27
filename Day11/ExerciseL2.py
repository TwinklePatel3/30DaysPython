#                               Exercises: Level 2

# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
def evens_and_odds(num):
    number_of_odds = 0
    number_of_evens = 0
    for i in range(num+1):
        if (i % 2 == 0):
            number_of_evens += 1
        else:
            number_of_odds += 1
    return f'The number of odds are {number_of_odds}.\nThe number of evens are {number_of_evens}'


print(evens_and_odds(100))
# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number


def factorial(num):
    fact = 1
    for i in range(num+1):
        if i > 0:
            fact *= i
    return fact


print(factorial(5))

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not


def is_empty(*para):
    if para:
        return False
    else:
        return True


print(is_empty())
print(is_empty(1))

# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).


def calculate_mean(list):
    len_number = len(list)
    total = sum(list)
    return total/len_number


def calculate_median(list):
    list.sort()
    len_of_list = len(list)
    middle_index_of_list = int(len_of_list/2)

    median = 0
    if len_of_list % 2 == 0:
        median = (list[middle_index_of_list-1] +
                  list[middle_index_of_list])/2
    else:
        median = list[middle_index_of_list]
    return median


def calculate_mode(list):
    uniq_values = []
    mode_values = []
    # print(max(list, key=list.count))
    for i in list:
        if i not in uniq_values:
            uniq_values.append(i)
        else:
            mode_values.append(i)
    if len(set(mode_values)) > 0:
        return set(mode_values)
    else:
        return "No modes"


def calculate_range(list):
    return max(list) - min(list)


def calculate_variance(list):
    variance = 0
    mean = calculate_mean(list)
    for item in list:
        variance += (item - mean)**2
    return variance/len(list)


def calculate_std(list):
    variance = calculate_variance(list)
    return variance ** 0.5


num_list = [35, 42, 39, 38, 43, 49, 42]
print("List :", num_list)
print("Mean :", calculate_mean(num_list))
print("Median :", calculate_median(num_list))
print("Mode :", calculate_mode(num_list))
print("Range :", calculate_range(num_list))
print("Variance :", calculate_variance(num_list))
print("Standard deviation :", calculate_std(num_list))
