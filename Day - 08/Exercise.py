#                            💻 Exercises: Day 8

# 1. Create an empty dictionary called dog
dog = dict()
print(dog)

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {"name": "Jackson", "color": "black",
       "breed": "Bull dog", "legs": 4, "age": 10}
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Twinkle",
    "last_name": "Patel",
    "gender": "Female",
    "age": 20,
    "martial_status": False,
    "skills": ["Pyhton", "ML", "NLP"],
    "country": "India",
    "city": "Mumbai",
    "Address": {
        "state": "Maharastra",
        "area": "Andheri"
    }
}

# 4. Get the length of the student dictionary
print("Length of the student dictionary :", len(student))

# 5. Get the value of skills and check the data type, it should be a list
value_of_skills = student["skills"]
print("Value of skills :", value_of_skills)
print("data type :", type(value_of_skills))

# 6. Modify the skills values by adding one or two skills
student["skills"].extend(["react", "react-native"])
print("Skills values :", student["skills"])

# 7. Get the dictionary keys as a list
print("Dictionary keys as a list :", student.keys())

# 8. Get the dictionary values as a list
print("Dictionary value as a list :", student.values())

# 9. Change the dictionary to a list of tuples using items() method
print("The dictionary to a list of tuples using items() :", student.items())

# 10. Delete one of the items in the dictionary
student.pop("age")
print(student)

# 11. Delete one of the dictionaries
del dog
