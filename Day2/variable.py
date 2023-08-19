#                       Exercises: Level 1

# 1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# 2. Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2: 30 Days of python programming
# 3. Declare a first name variable and assign a value to it
first_name = "Twinkle"
# 4. Declare a last name variable and assign a value to it
last_name = "Patel"
# 5. Declare a full name variable and assign a value to it
full_name = "Twinkle Patel"
# 6. Declare a country variable and assign a value to it
country = "India"
# 7. Declare a city variable and assign a value to it
city = "Mumbai"
# 8. Declare an age variable and assign a value to it
age = 20
# 9. Declare a year variable and assign a value to it
year = 2023
# 10. Declare a variable is_married and assign a value to it
is_married = False
# 11. Declare a variable is_true and assign a value to it
is_true = True
# 12. Declare a variable is_light_on and assign a value to it
is_light_on = False
# 13. Declare multiple variable on one line
city, landmark, is_open, contact_number = "Mumbai","Temple",False,"7887878787"


#                        Exercises: Level 2

# 1. Check the data type of all your variables using type() built-in function
print(type(city))
print(type(landmark))
print(type(is_open))
print(type(contact_number))

# 2. Using the len() built-in function, find the length of your first name
print("length of your first name",len(first_name))

# 3. Compare the length of your first name and your last name
print(min(len(first_name),len(last_name)))
print(max(len(first_name),len(last_name)))

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#   -  Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print("total =",total)
#   -  Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print("diff = ",diff)
#   -  Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print("product = ", product)
#   -  Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two
print("division =",division)
#   -  Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two%num_one
print("remainder =",remainder)
#   -  Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print("exp =",exp)
#   -  Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print("floor_division =",floor_division)
# 5. The radius of a circle is 30 meters.
radius = 30
#   -  Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14*(30**2)
print("area of circle = ",area_of_circle)
#   -  Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*3.14*30
print("circumference of circle =",circum_of_circle)
#   -  Take radius as user input and calculate the area.
usr_radius = input("Enter radius : ")
area = 3.14*(int(usr_radius)**2)
print("Inputted Radius =",usr_radius)
print("Area = ",area)
# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
country = input("Enter your country : ")
age = input("Enter your age : ")

print("Your fullname is ",first_name ,last_name,",", age, "year old lived in", country )
# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
print(help('keywords'))