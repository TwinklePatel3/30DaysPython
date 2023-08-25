a = 3
if a > 0:
    print("A is positive number")

# If Else
if a < 0:
    print("A is negative number")
else:
    print("A is positive number")

# If Elif Else

a = 0
if a > 0:
    print("A is positive number")
elif a < 0:
    print("A is negative number")
else:
    print("A is zero")


# Short Hand
# code if condition else code
a = 3
print("A is positive") if a > 0 else print("A is negative")

a = 4
if a > 0:
    if a % 2 == 0:
        print("A is positive and even number")
    else:
        print("A is positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is negative")

if a > 0 and a % 2 == 0:
    print("A is positive and even number")
elif a < 0 and a % 2 != 0:
    print("A is positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is negative")
