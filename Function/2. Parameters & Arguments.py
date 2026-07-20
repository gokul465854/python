from os import name


def greet(name):
    print("Hello",name)

greet("Jai")
greet("sakshi")
greet("kundan")
greet(True)
greet(1)
greet(3.4)
# greet(input("Enter name: "))

# Multiple Parameters
def sum3(a,b):
    print(a + b)
sum3(1,2)
sum3("jai","sakshi")
# sum("jai",2) --> TypeError: can only concatenate str (not "int") to str

# Positional Arguments
# Python matches arguments by their position.
def info(name,city):
    print(name,city)
info("jai","pune")
# wrong order
info("pune","jai")

# Keyword Arguments
def info(name,city):
    print(name,city)
info(name="Jai",city="pune")
info(city="pune",name="jai")
info(1,2)
info(name=1,city=3)

# Default Arguments
# A default value is used if the caller doesn't provide one.
def greet(name = "jai"):
    print("Hello",name)
greet()

# Multiple Default Arguments
def student(name, city="Mumbai", age=18):
    print(name)
    print(city)
    print(age)

student("Gokul")

# Default Argument Rule
# correct:
def student(name,age=18):
    pass
# incorrect
# def student1(age=18,name): --> ''' SyntaxError: parameter without a default follows parameter with a default '''
    # print(age,name)
# student1("jai")

# Variable-Length Positional Arguments (*args)
def numbers(*args):
    print(args)
numbers(1)
numbers(1,2,3)
numbers(1,2,3,4,5,6,6)

# example
def sum1(*args):
    print(sum(args))
sum1(1,2)
sum1(1,2,3)
sum1(1,2,3,4,5)

# Variable-Length Keyword Arguments (**kwargs)
# **kwargs collects extra keyword arguments into a dictionary.

def data(**kwargs):
    print(kwargs)
    print(type(kwargs))
data(name="jai",age=43,city="pune",state="maharastra")



