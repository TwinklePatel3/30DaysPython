#                               Exercises: Level 2

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num):
    from random import choices
    import string
    hexa_colors_list = []

    for i in range(num):
        hexa_colors_list.append(
            "#"+"".join(choices(string.hexdigits.upper(), k=6)))
    return hexa_colors_list


print(list_of_hexa_colors(5))
# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.


def list_of_rgb_colors(num):
    from random import randint

    rgb_colors_list = []
    for i in range(num):
        rgb_colors_list.append(
            f'rgb({randint(0,255)}, {randint(0,255)}, {randint(0,255)})')
    return rgb_colors_list


print(list_of_rgb_colors(5))

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']


def generate_colors(color, num_pair):
    str(color).lower
    if color == "hexa" and type(num_pair) == int:
        return list_of_hexa_colors(num_pair)
    elif color == "rgb" and type(num_pair) == int:
        return list_of_rgb_colors(num_pair)
    else:
        return "Enter valid color type:'hexa' or 'rgb' and number of list item."


print(generate_colors('hxa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))
print(generate_colors('rgb', "1"))
