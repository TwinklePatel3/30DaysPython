#                             💻 Exercises: Day 18

#                               Exercises: Level 1
import re

# 1. What is the most frequent word in the following paragraph?
#     paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
#     [
#     (6, 'love'),
#     (5, 'you'),
#     (3, 'can'),
#     (2, 'what'),
#     (2, 'teaching'),
#     (2, 'not'),
#     (2, 'else'),
#     (2, 'do'),
#     (2, 'I'),
#     (1, 'which'),
#     (1, 'to'),
#     (1, 'the'),
#     (1, 'something'),
#     (1, 'if'),
#     (1, 'give'),
#     (1, 'develop'),
#     (1, 'capabilities'),
#     (1, 'application'),
#     (1, 'an'),
#     (1, 'all'),
#     (1, 'Python'),
#     (1, 'If')
#     ]
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = re.findall('\w+', paragraph)
match_count = []
count = 0
for word in set(words):
    for match in words:
        if word == match:
            count += 1
    match_count.append((count, word))
    count = 0

print(sorted(match_count, reverse=True))

# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
# points = ['-12', '-4', '-3', '-1', '0', '4', '8']
# sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 -(-12) # 20
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. '
# points = ['-12', '-4', '-3', '-1', '0', '4', '8']
# sorted_points = [-12, -4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 - (-12)  # 20
points = re.findall('-?\d+', txt)
sorted_points = sorted(list(map(int, points)))
print("points = ", points)
print("sorted_points = ", sorted_points)
print(
    f'distance = {max(sorted_points)} - {min(sorted_points)} = {max(sorted_points) - min(sorted_points)}')
