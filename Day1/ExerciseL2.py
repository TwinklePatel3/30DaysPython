# Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file ExerciseL2.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

# 1. Check the python version you are using
import platform #to check python version
print(platform.python_version()) #3.11.2

#2. Open the python interactive shell and do the following operations. The operands are 3 and 4.

print(3 + 4)  #7   # addition(+)
print(4 - 3)  #1   # subtraction(-)
print(3 * 4)  #12   # multiplication(*)
print(4 % 3)  #1   # modulus(%)
print(4 / 3)  #1.3333333333333333  # division(/)
print(3 ** 4) #81  # exponential(**)
print(4 // 3) #1  # floor division operator(//)

#3. Write strings on the python interactive shell. The strings are the following:
print("Twinkle")    # Your name
print("Patel")      # Your family name
print("India")      # Your country
print("I am enjoying 30 days of python")    # I am enjoying 30 days of python1

# 4. Check the data types of the following data:
# 10
print(type(10))     #<class 'int'>
# 9.8
print(type(9.8))    #<class 'float'>
# 3.14
print(type(3.14))   #<class 'float'>
# 4 - 4j
print(type(4-4j))   #<class 'complex'>
# ['Asabeneh', 'Python', 'Finland']
print(type(['Asabeneh', 'Python', 'Finland']))  #<class 'list'>
# Your name
print(type("Twinkle"))  #<class 'str'>
# Your family name
print(type("Patel"))    #<class 'str'>
# Your country
print(type("India"))    #<class 'str'>
