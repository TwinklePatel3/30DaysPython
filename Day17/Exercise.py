#                                 Exercises: Day 17

# 1. names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'].
#  Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway',
         'Denmark', 'Iceland', 'Estonia', 'Russia']
*nordic_countries, es, ru = names

print(f'Nordic country are {nordic_countries}, es and ru are {es} {ru}')
