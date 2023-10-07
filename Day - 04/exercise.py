#                               💻 Exercises - Day 4

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
text = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
print(text)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
text1 = 'Coding ' + 'For ' + 'All'
print(text1)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print("length of the company is ", len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print("uppercase letters :", company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print("lowercase letters :", company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print("capitalize() :", company.capitalize())
print("title() : ", company.title())
print("swapcase() :", company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding For All string contains a word Coding :", company.index("Coding"))
print("Coding For All string contains a word Coding :", company.find("Coding"))
print("Coding For All string contains a word Coding :", company.rfind("Coding"))
print("Coding For All string contains a word Coding :", company.rindex("Coding"))
print("Coding For All string contains a word Coding : ", "Coding" in company)
print(company.count("Coding"))

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
text = "Python For Everyone"
print(text.replace("Everyone", "All"))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company_names = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company_names.split(","))

# 15. What is the character at index 0 in the string Coding For All.
print("character at index 0 in the string \"Coding For All\" :", company[0])

# 16. What is the last index of the string Coding For All.
print("Last index of the string \"Coding For All\" : ", len(company)-1)

# 17. What character is at index 10 in "Coding For All" string.
print("Character at index 10 in \"Coding For All\" is ", company[10])  # space

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym = text.split(" ")
print("An acronym or an abbreviation for the name 'Python For Everyone' :",
      acronym[0][0] + acronym[1][0] + acronym[2][0])

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
abbreviation = company.split(" ")
print("An acronym or an abbreviation for the name 'Coding For All' :",
      abbreviation[0][0] + abbreviation[1][0] + abbreviation[2][0])

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print("The position of the first occurrence of \"C\" in \"Coding For All\" : ",
      company.index("C"))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print("The position of the first occurrence of \"F\" in \"Coding For All\" : ",
      company.index("F"))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
text = "Coding For All People"
print("The last occurrence of \"l\" in \"Coding For All People\" :", text.rfind("l"))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print("The position of the first occurrence of the word 'because' in sentence :",
      sentence.find("because"), sentence.index("because"))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("The position of the last occurrence of the word 'because' in sentence :",
      sentence.rindex("because"))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:55])

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("The position of the first occurrence of the word 'because' in sentence :",
      sentence.find("because"), sentence.index("because"))

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:55])

# 28. Does ''Coding For All' start with a substring Coding?
print("Does ''Coding For All' start with a substring Coding : ",
      company.startswith("Coding"))

# 29. Does 'Coding For All' end with a substring coding?
print("Does 'Coding For All' end with a substring coding :",
      company.endswith("coding"))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
space_text = '   Coding For All      '
print(space_text.strip("  "))

# 31. Which one of the following variables return True when we use the method isidentifier():
#           30DaysOfPython
#           thirty_days_of_python
print("30DaysOfPython".isidentifier())  # False
print("thirty_days_of_python".isidentifier())  # true

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(python_lib))

# 33. Use the new line escape sequence to separate the following sentences.
#           I am enjoying this challenge.
#           I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Use a tab escape sequence to write the following lines.
#           Name      Age     Country   City
#           Asabeneh  250     Finland   Helsinki
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
# 35. Use the string formatting method to display the following:
#           radius = 10
#           area = 3.14 * radius ** 2
#           The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(
    f'The area of a circle with radius {radius} is {int(area)} meters square.')

# 36. Make the following using string formatting methods:
#           8 + 6 = 14
#           8 - 6 = 2
#           8 * 6 = 48
#           8 / 6 = 1.33
#           8 % 6 = 2
#           8 // 6 = 1
#           8 ** 6 = 262144
num_1 = 8
num_2 = 6
print(f'{num_1} + {num_2} = {num_1+num_2}')
print(f'{num_1} - {num_2} = {num_1-num_2}')
print(f'{num_1} * {num_2} = {num_1*num_2}')
print(f'{num_1} / {num_2} = {num_1/num_2:.2f}')
print(f'{num_1} % {num_2} = {num_1%num_2}')
print(f'{num_1} // {num_2} = {num_1//num_2}')
print(f'{num_1} ** {num_2} = {num_1**num_2}')
