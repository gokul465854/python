# Docstring (Documentation String)
# access docstring
def square(x):
    """Return square of number."""
    return x * x
print(square.__doc__)

# help() Function
# Python automatically docstring ko pretty format me dikhata hai
def add(a,b):
    """Addition of two numbers."""
    return a + b
help(add)

# Multi-line Docstring
def factorial(n):
    """
    Calculate factorial of n
    :parameter:
         n(int): positive integer
    :return:
         int: factorial of n
    """
    return 1 if n == 0 else n * factorial(n-1)

help(factorial)
print(factorial.__doc__)
print(factorial(5))

# good example:
def sum3(a,b):
    """
    Returns the sum of two numbers
    :param a: (int) first number
    :param b: (int) second number
    :return: (int) sum of a and b
    """
    return a + b
help(sum3)

# type Hints --> Type Hint batata hai ki function kis type ka data expect karta hai.
def cube(a: int):
    """
    Return the cube of number
    :param a: integer
    :return: cube of a
    """
    return a ** 3
help(cube)
print(cube(3))

# Return type hint
def multiply(a: int,b: int) -> int:
    """
    Returns multiplication of two numbers
    :param a: first number
    :param b: second number
    :return: multiply of two a and b
    """
    return a * b
help(multiply)
print(multiply(3,4))

def is_even(n: int) -> bool:
    """
    Return the boolean of n is even or odd
    :param n: integer
    :return: if even return n as even or not
    """
    return True if n % 2 == 0 else False

print(is_even(3))

# list type hint
def total(numbers: list[int]) -> int:
    """
    Return sum of list element
    :param numbers: list
    :return: sum of all element
    """
    return sum(numbers)
print(total([1,2,3,4,5]))

# Dictionary Type Hint
def data() -> dict[str,int]:
    return {
        "jai": 24,
        "sakshi": 69,
        "kundan": 80
    }
print(data())

# tuple type hint
def point() -> tuple[int]:
    return (10,20,67,879,57,98,899)
print(point())

# complex example
def employee(
        name:str,
        age:int,
        salary:float
) -> str:
    """ Returns Employee details"""
    return f"Name: {name}, Age: {age}, Salary: {salary}"

print(employee("Jai",22,90000.45))