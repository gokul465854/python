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