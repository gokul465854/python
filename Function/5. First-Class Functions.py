from dis import code_info
from random import choice
from subprocess import check_output
from xml.dom.minidom import ProcessingInstruction


def demo():
    print("first class function")
print(type(demo)) # --> <class 'function'>

# pass the multiple function
def add():
    print("Addition")
def sub():
    print("Subtraction")
def calculator(operations):
    operations()
calculator(add)
calculator(sub)

# function return other function
def outer():
    def inner():
        print("hello")
    return inner
x = outer()
x()

# store function in the list
def add():
    print("add")
def sub():
    print("sub")
operations = [add,sub]
operations[0]()
operations[1]()
print(type(operations))

# function in the dictionary
def login():
    print("login")
def logout():
    print("logout")
menu = {
    1: login,
    2: logout
}

choice = 1
menu[choice]()
choice = 2
menu[choice]()

# function as callback
def success():
    print("payment successful")

def payment(callback):
    print("processing payment.....")
    callback()

payment(success)


