from math import radians, sin , cos

# To find the sine and cosine of a specific angle initially expressed in degrees, we can call the radians function to convert it to radians, and then call the sine and cosine functions, passing the angle in radians:

angle_degrees = 40
angle_radians = radians(angle_degrees)

sin_value = sin(angle_radians)
cos_value = cos(angle_radians)
 
print(sin_value) # 0.6427876096865393
print(cos_value) # 0.766044443118978


# For example, if you do this while importing the math module, you'll be able to call any function defined in that module without specifying the name of the module as a prefix. Here are some examples:
from math import *

print(sqrt(35))
print(pow(3, 2))
print(exp(1))

# mport statements work exactly the same for functions, classes, constants, variables, and any other elements defined in the module.
# Here is an example of a constant from the math module, the number pi:
import math
print(math.pi)

# And here is an example of a class from the datetime module. We create a date object that represents July 15, 1959. Then, we assign that date object to a variable and access the day, month, and year individually using dot notation:
import datetime
birthday = datetime.date(2004,8,31)

print(birthday.day)
print(birthday.month)
print(birthday.year)