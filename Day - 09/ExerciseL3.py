#                                   Exercises: Level 3

# 1. Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ["JavaScript", "React", "React", 'Node', 'MongoDB', ],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    middleIndex = int(len(person['skills'])/2)
    print("Middle skill :", person['skills'][middleIndex])
else:
    print("person dictionary has no skills key")
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    print("person has 'Python' skill ?", "Python" in person['skills'])
else:
    print("person dictionary has no skills key")

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if "skills" in person:
    if sorted(person["skills"]) == sorted(["JavaScript", "React"]):
        print("He is a front end developer")
    elif sorted(person["skills"]) == sorted(["Node", "Python", "MongoDB"]):
        print("He is a back end developer")
    elif sorted(person["skills"]) == sorted(["Node", "React", "MongoDB"]):
        print("He is a full stack developer")
    else:
        print("Unknown title")
else:
    print("person dictionary has no skills key")

#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

if person["is_marred"] == True and person["country"]:
    print(
        f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married')
else:
    print("Either the person is not married or he is not lived in Finland.")
