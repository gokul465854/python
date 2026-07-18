base = int(input("enter the base of triangle: "))
height = int(input("enter the height of triangle: "))
hypotenuse = int(input("enter the hypotenuse of triangle: "))

print("It is a triangle" if (hypotenuse ** 2 == (base ** 2) + (height ** 2)) else "Not triangle")