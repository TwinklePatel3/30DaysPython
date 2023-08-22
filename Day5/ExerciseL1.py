#                                        💻 Exercises: Day 5

#                                           Exercises: Level 1

# 1. Declare an empty list
lst = []
lst = list()
print(len(lst))

# 2. Declare a list with more than 5 items
lst = ["item1", "item2", "item3", "item4", "item5", "item6", "item7"]

# 3. Find the length of your list
print(len(lst))

# 4. Get the first item, the middle item and the last item of the list
print("first Item :", lst[0])
print("Middle Item :", lst[int(len(lst)/2)])
print("Last Item :", lst[-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Twinkle", 20, 5.5, "Single", "India"]
print(mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]
# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print("Number of companies :", len(it_companies))

# 9. Print the first, middle and last company
print("first company :", it_companies[0])
print("Middle company :", it_companies[int(len(it_companies)/2)])
print("Last company :", it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Infosys")
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies)/2), "TCS")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
lst = "#; ".join(it_companies)
print(lst)

# 15. Check if a certain company exists in the it_companies list.
print("Does exists 'Apple' in list :", "Apple" in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
print(it_companies[0:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
middleIndex = int(len(it_companies)/2)
print(it_companies[middleIndex])

# 21. Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(int(len(it_companies)/2))
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies
# generate error (NameError: name 'it_companies' is not defined) as it is destroyed
# print(it_companies)

# 26. Join the following lists:
#       front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#       back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
tech = back_end + front_end
print(tech)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = tech.copy()
full_stack.extend(["Python", "SQL"])
print("tech :", tech)
print("full_stack :", full_stack)
