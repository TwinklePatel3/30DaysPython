#                           💻 Exercises: Day 6

#                           Exercises: Level 1

# 1. Create an empty tuple
empty_tuple = tuple()
print(empty_tuple)

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Alice", "Bob", "Charlie")
sister = ("Ana", "Barbie", "Cia")

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sister
print(siblings)

# 4. How many siblings do you have?
print("Total siblings :", len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# Modification of tuple is not possible.
# To perform this task we can do this by convert it to list.

siblingslst = list(siblings)
siblingslst.extend(["John", "Jenny"])
family_members = tuple(siblingslst)

print(family_members)


#                           Exercises: Level 2

# 1. Unpack siblings and parents from family_members
# family_members is from ExerciseL1.py
*siblings, father, mother = family_members
print(father, mother)

# REST SOLUTION IN EXERCISEL2.PY
