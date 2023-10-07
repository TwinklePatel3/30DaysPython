#                                   💻 Exercises: Level 2

# # sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Join A and B
C = A.union(B)
print(C)

# 2. Find A intersection B
print("A intersection B :", A.intersection(B))

# 3. Is A subset of B
print("Is A subset of B ?", A.issubset(B))

# 4. Are A and B disjoint sets
print("Are A and B disjoint sets ?", A.isdisjoint(B))

# 5. Join A with B and B with A
A.update(B)
print("A with B :", A)
B.update(A)
print("B with A :", B)

# 6. What is the symmetric difference between A and B
# We got set() as we have join them in previous question. Comment 5th solution and try again,you got {27,28}
print("The symmetric difference between A and B :", A.symmetric_difference(B))

# 7. Delete the sets completely
del A, B, C
