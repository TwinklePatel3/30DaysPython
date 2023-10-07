#                               Exercises: Level 2
import re

# 1. Write a pattern which identifies if a string is a valid python variable

# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True


def is_valid_variable(var):
    reg_pattern = r'^[a-zA-Z_]\w*$'
    if re.findall(reg_pattern, var):
        return True
    else:
        return False


print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))  # True
print(is_valid_variable('_firstname'))  # True
