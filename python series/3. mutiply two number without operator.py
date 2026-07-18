 # write program that can multiple two numbers without * operator

import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))

multiply = math.prod([a,b])
print(f"{a} X {b} = {multiply}")