# Creating a Dictionary
empty_dict = {}
person = {
    "first_name": "Twinkle",
    "last_name": "Patel",
    "is_married": False,
    "age": 20,
    "hobby": ["Reading", "playing games", "music", "drawing"],
    "address": {
        "state": "Maharastra",
        "country": "India"
    }
}

# lenght
print(len(person))

# Accessing Dictionary Items
print(person["first_name"])
print(person["hobby"])
print(person["address"]["state"])
# print(person["city"])  # error

# Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.
print(person.get("last_name"))
print(person.get("hobby"))
print(person.get("city"))
print(person.get("address"))

# Adding Items to a Dictionary
person["JobTitle"] = "Developer"
person["hobby"].append("Dancing")

print(person)

#  modification of dictionary
person["JobTitle"] = "Software developer"
person["age"] = 21
print(person)

# Checking Keys in a Dictionary
print("age" in person)
print("City" in person)

# Removing Key and Value Pairs from a Dictionary

# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name

person.pop("age")
person.popitem()
del person["hobby"]

# Changing Dictionary to a List of Items

print(person)
print(person.items())

# Clearing a Dictionary
print(person.clear())

# Deleting a Dictionary
del person

# Copy a Dictionary
person = {
    "first_name": "Twinkle",
    "last_name": "Patel",
    "is_married": False,
    "age": 20,
    "hobby": ["Reading", "playing games", "music", "drawing"],
    "address": {
        "state": "Maharastra",
        "country": "India"
    }
}

person_cpy = person.copy()
print(person_cpy)

# Getting Dictionary Keys as a List
print(person.keys())
print(person.values())
