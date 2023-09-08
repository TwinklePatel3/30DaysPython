class Person:
    def __init__(self, name) -> None:
        self.name = name


p = Person("Twinkle")
print(p.name)


class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


p = Person("Twinkle", "Patel", 21, "India", "Mumbai")
print(p.firstname)
print(p.lastname)
print(p.city)


class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old, lives in {self.city}, {self.country}'


p = Person("Twinkle", "Patel", 21, "India", "Mumbai")
print(p.person_info())
