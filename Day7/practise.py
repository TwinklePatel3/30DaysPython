st = set()  # Creating an empty set
st = {'item1', 'item2', 'item3', 'item4'}  # Creating a set with initial items
fruits = {'banana', 'orange', 'mango', 'lemon'}
# To check if an item exist in a list we use in membership operator.
print("Does exists ?", "orange" in fruits)
fruits.add("Apple")  # Add one item using add()
print(fruits)

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
fruits.update(["kiwi", "lime"])
print(fruits)
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)

# The pop() methods remove a random item from a list and it returns the removed item.
fruits.pop()
print(fruits)
removed_item = fruits.pop()
print(removed_item)

fruits.clear()  # Clearing Items in a Set
del fruits  # delete the set itself we use del operator.

# Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)
print(fruits)

# We can join two sets using the union() or update() method.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

# Finding Intersection Items

st2Int = {"item1", "item3", "item5"}
inter = st1.intersection(st2Int)
print(inter)

# Checking Subset and Super Set

stsubset = {'item1',  'item3'}
print(st2Int.issubset(st1))
print(st1.issubset(st2Int))

print(st2Int.issuperset(st1))
print(st1.issuperset(stsubset))

# Checking the Difference Between Two Sets

print(st2Int.difference(st1))
print(stsubset.difference(st1))
print(st1.difference(st2Int))
print(st1.difference(stsubset))

# Finding Symmetric Difference Between Two Sets

print(st2Int.symmetric_difference(st1))
print(stsubset.symmetric_difference(st1))
print(st1.symmetric_difference(st2Int))
print(st1.symmetric_difference(stsubset))

# Joining Sets
# If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
print(stsubset.isdisjoint(st1))
print(st1.isdisjoint(st2Int))

st4 = {"item7", "item8", "item10"}
print(st1.isdisjoint(st4))
print(st2.isdisjoint(st4))
