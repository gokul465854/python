from codeop import compile_command
from idlelib import config


def sumOfDigit(*args):
    return sum(args)
total = sumOfDigit(1,2,3,4,5)
print(total)

# Returning Multiple Values
def student():
    return "Jai",21,"pune"
data = student()
print(data)
# Unpacking Returned Values
name,age,city = student()
print(name)
print(age)
print(city)

# Returning a List
def number():
    return [1,2,3,4,5]
l = number()
print(l)

# return dictionary
def profile():
    return {
        "name": "jai",
        "age": 33,
        "city": "pune"
    }
print(profile())
name,age,city = profile().items()
print(name)
print(age)
print(city)

def compare(a,b):
    if a > b:
        return "a is greater than b"
    elif a < b:
        return "b is greater than a"
    else:
        return "a and b are equal"
# print(compare(1,2))
# print(compare(4,2))
# print(compare(2,2))
# print(compare(True,False))
# print(compare("jai","sakshi"))
# print(compare("a","b"))
# print(compare("ab","ac"))
# print(compare("10","2"))



