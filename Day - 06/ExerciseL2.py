#                           Exercises: Level 2

# 1. Unpack siblings and parents from family_members
# SOLUTION is in ExerciseL1.py of Day6

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Apple", "Banana", "Chickoo", "Dates")
vegetables = ("Avacado", "Beetroot", "Carrot")
animal = ("Tiger", "Lion", "Jaguar", "Chetaah")
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = int(len(food_stuff_tp)/2)
print("Middle Item :", food_stuff_tp[middle_index])

# 5. Slice out the first three items and the last three items from food_staff_lt list
print("First three items :", food_stuff_lt[0:3])
print("Last three items :", food_stuff_lt[-3:])

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
#       Check if 'Estonia' is a nordic country
#       Check if 'Iceland' is a nordic country
#       nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Is 'Estonia' is a nordic country ?", "Estonia" in nordic_countries)
print("Is 'Iceland' is a nordic country ?", "Iceland" in nordic_countries)
