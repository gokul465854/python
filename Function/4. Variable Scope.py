'''
types of scope:
1. Local
2. Enclosing
3. Global
4. Built-in
together they form the LEGB rule
'''

# local scope (L)
# A variable created inside a function belongs only to that function.
def name():
    name = "jai" #--> local scope
    print(name)
name()

# Global scope (G)
# Variables created outside all functions are global variables.
college = "ABC college" # --> global scope
def show():
    print(college)
show()
print(college)

# Local Variable Shadows Global Variable
name = "jai"
def showName():
    name = "Sakshi"
    print(name)
showName()
print(name)

# Reading vs Modifying Global Variables
# reading:
x = 10
def read():
    print(x)
read()

# modifying:
y = 10
def modify():
    pass
    # y += 1 --> UnboundLocalError: cannot access local variable 'y'
                   # where it is not associated with a value
modify()

# modifying correctly
z = 10
def correctWay():
    global z
    z += 1
correctWay()
print(z)

# Enclosing Scope (E)
# An enclosing scope exists when one function is inside another.
def outer():
    x = 100
    def inner():
        print(x)
    inner()
outer()

# nonlocal Keyword --> Suppose you want to modify a variable from the enclosing function.
def outerFun():
    x = 100
    def innerFun():
        nonlocal x
        x += 5
    innerFun()
    print(x)
outerFun()

# Built-in Scope (B) --> Python automatically provides built-in names
'''
Examples:
print()
len()
sum()
max()
min()
range()
These come from Python's built-in namespace.
'''

'''
LEGB Rule
When Python looks for a variable, it searches in this order:
L → Local
↓
E → Enclosing
↓
G → Global
↓
B → Built-in
'''
# Example:
x = "Global"

def outer():

    x = "Enclosing"

    def inner():

        x = "Local"

        print(x)

    inner()

outer()