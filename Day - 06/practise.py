empty_tuple = ()
empty_tuple = tuple()
tp1 = ("item1", "item2", "item3", "item4")
len(tp1)
print("First item : ", tp1[0])
print("Second item :", tp1[1])
last_index = len(tp1) - 1
print("last item :", tp1[last_index])

# using negative index
print("First item : ", tp1[-4])
print("Second item :", tp1[-3])
print("last item :", tp1[-1])

# slicing
print("All items :", tp1[0:4])
print("All items :", tp1[0:])
print("Middle items :", tp1[1:3])
print("All items :", tp1[-4:])
print("Middle items :", tp1[-3:-1])

# Changing Tuples to Lists

tpl = list(tp1)

# Checking an Item in a Tuple

print("item1" in tp1)
