def a():
    b()
def b():
    c()
def c():
    print("Done")

# c()

def add(a,b):
    print(a+b)

add(3,4)

def test(a,b):
    print(a,b)
test(23,b=67)

# Calling One Function from Another
def line():
    print('-' * 20)
def menu():
    line()
    print("1. Add")
    print("2. Delete")
    print("3. Exit")
    line()

menu()

# Create three functions:
# breakfast()
# lunch()
# dinner()
# Call them in order.
def breakfast():
    print("eat breakfast")
def lunch():
    print("eat lunch")
def dinner():
    breakfast()
    lunch()
    print("eat dinner")

dinner()















