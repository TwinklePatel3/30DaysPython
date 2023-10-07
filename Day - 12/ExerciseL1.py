#                              💻 Exercises: Day 12

#                               Exercises: Level 1

# 1. Write a function which generates a six digit/character random_user_id.
#   print(random_user_id());
#   '1ee33d'
def random_user_id():
    from random import randint
    user_id = randint(111111, 999999)
    return user_id


print(random_user_id())
# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf

# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr


def user_id_gen_by_user():
    num_of_digits = input("Enter number of characters :")
    num_of_userId = input("How many ids to generate ?")
    from random import randint, choices
    import string
    for i in range(int(num_of_userId)):
        user_id = "".join(choices(string.ascii_letters +
                          string.digits, k=int(num_of_digits)))
        print(user_id)


print(user_id_gen_by_user())

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form


def rgb_color_gen():
    from random import randint
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return f'rgb({r},{g},{b})'


print(rgb_color_gen())
