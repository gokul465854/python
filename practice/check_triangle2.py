side1 = int(input("Enter a side 1: "))
side2 = int(input("Enter a side 2: "))
side3 = int(input("Enter a side 3: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("the sides are form valid triangle")
    if side1 == side2 == side3:
       print("It is a Equilateral Triangle")
    elif side1 == side2 or side2 == side3 or side3 == side1:
       print("It is isosceles Triangle")
    else:
       print("It is scalene Triangle")
else:
    print("The sides are not form valid triangle")