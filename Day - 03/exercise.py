#                                   💻 Exercises - Day 3

# 1. Declare your age as integer variable
age = 20


# 2. Declare your height as a float variable
height = 5.4

# 3. Declare a variable that store a complex number
complex_num = 1 + 1j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100
base = input("Enter base : ")
height = input("Enter height : ")
area = 0.5 * float(base) * float(height)
print ("The area of the triangle is",int(area))

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
#   Calculate the perimeter of the triangle (perimeter = a + b + c).
#   Enter side a: 5
#   Enter side b: 4
#   Enter side c: 3
#   The perimeter of the triangle is 12
side_a = input("Enter side a : ")
side_b = input("Enter side b : ")
side_c = input("Enter side c : ")
perimeter_of_triangle = int(side_a)+int(side_b)+int(side_c)
print("The perimeter of the triangle is",perimeter_of_triangle)

# 6. Get length and width of a rectangle using prompt. 
#   Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
len_of_reactangle = int(input("Enter lenght of reactangle : "))
width_of_reactangle = int(input("Enter width of reactangle : "))
area_of_reactangle = len_of_reactangle * width_of_reactangle
perimeter_of_reactangle = 2*(len_of_reactangle+width_of_reactangle)
print("Area of reactangle is ",area_of_reactangle)
print("Perimeter of reactangle is ",perimeter_of_reactangle)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius = int(input("Enter radius of circle : "))
print("Area of circle is ", pi*radius*radius)
print("circumference of circle is ",2*pi*radius)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# y=mx+b
slope_1 = 2

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1,x2,y1,y2 = 2,6,2,10
slope_2 = ((y2 - y1) / (x2 - x1))
#formula = d = √((x2-x1)2 + (y2-y1)2)
euclidean_distance = ((x2 - x1)**2+(y2-y1)**2)**0.5
print("slope",slope_2)
print("Euclidean_distance",euclidean_distance)

# 10. Compare the slopes in tasks 8 and 9.
print(slope_1 == slope_2)

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
print("y =",x**2+6*x+9)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len('python')
len_dragon = len("dragon")
print(len_python != len_dragon)

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("'on' is found in both 'python' and 'dragon'","on" in "python" and "on" in "dragon")

# 14. I hope this course is not full of jargon. 
#   Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")

# 15. There is no 'on' in both dragon and python
print("There is no 'on' in both dragon and python","on" not in "python" and "on" not in "dragon")

# 16. Find the length of the text python and convert the value to float and convert it to string
print(float(len_python),str(len_python))

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num=10
is_Even = num % 2 == 0
print(is_Even)

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print(type('10')==type(10))

# 20. Check if int('9.8') is equal to 10
# print(int('9.8') == 10) #Error

# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#       Enter hours: 40
#       Enter rate per hour: 28
#       Your weekly earning is 1120
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
print("Your weekly earning is ",hours*rate_per_hour)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
#       Enter number of years you have lived: 100
#       You have lived for 3153600000 seconds.
second_per_year = 60 * 60 * 24 * 365
num_of_yr = input("Enter number of years you have lived: ")
print("You have lived for",second_per_year * int(num_of_yr),"seconds")
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")