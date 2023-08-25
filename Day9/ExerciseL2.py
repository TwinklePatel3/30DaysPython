# ###                       Exercises: Level 2

# 1. Write a code which gives grade to students according to theirs scores:
#       80-100, A
#       70-89, B
#       60-69, C
#       50-59, D
#       0-49, F
score = int(input("Enter your score :"))
if score <= 100 and score >= 80:
    print("A")
elif score < 80 and score >= 70:
    print("B")
elif score < 70 and score >= 60:
    print("C")
elif score < 60 and score >= 50:
    print("D")
else:
    print("F")

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter month :")
if month == "September" or month == "October" or month == "November":
    print("The season is Autumn")
elif month == "December" or month == "January" or month == "February":
    print("The season is Winter")
elif month == "March" or month == "April" or month == "May":
    print("The season is Spring")
elif month == "June" or month == "July" or month == "August":
    print("The season is Summer.")

# 3. The following list contains some fruits:
#       fruits = ['banana', 'orange', 'mango', 'lemon']
#       If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
#       If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit : ")
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(fruits)
