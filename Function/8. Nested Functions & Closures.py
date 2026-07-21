#nested function
# def outer():
#     name = "jai"
#     def inner():
#         print(name)
#     inner()
# outer()
from itertools import count


# Closure
def outer():
    greet = "hello"
    def inner():
        print(greet)
    return inner
# func = outer()
# func()

# Function Factory --> Closure ka sabse common use
def multiplayer(n):
    def multiply(x):
        return x * n
    return multiply

n = multiplayer(5)
print(n(3))

# closure with greeting
def greeting(name: str) ->str :
    def say():
        print(f"Hello {name}")
    return say
g1 = greeting("jai")
g2 = greeting("sakshi")
g1()
g2()

# Closure ka sabse common use

def counter():
    count = 1
    def increament():
        nonlocal count
        count += 1
        print(count)
    return increament
c = counter()
c()
c()
c()

# check closure
def outer_fun():
    x = 100
    def inner_fun():
        print(x)
    return inner_fun
check = outer_fun()
print(check.__closure__[0].cell_contents)

# create login function factory
def login_factory(correct_password:str) -> str:
    def login(username,passaword):
        if passaword == correct_password:
            print(f"Welcome {username}")
        else:
            print("Invalide passaword")
    return login

login = login_factory("Gokul@46585")
login("Gokul","Gokul@46585")
login("gokul","1234")

# Tax collector closure
def tax_calculator(rate):
    def calculator(salary:float | int) -> float | int:
        return salary * rate / 100
    return calculator
gst = tax_calculator(18)
print(gst(50000))

# Temperature Converter Closur
def temp_converter(mode:str):
    """
    Returns a temperature converter function
    modes:
         C_to_F: Celsius to Fehrenheit
         F_to_C: Fehrenheit to Celsius
    """
    def convert(temp: float) -> float | str:
        if mode == "C_to_F":
            return  (temp * 9 / 5) + 32
        elif mode == "F_to_C":
            return (temp - 32) * 5 / 9
        else:
            return  "Invalid temperature"
    return convert

c_to_f = temp_converter("C_to_F")
f_to_c = temp_converter("F_to_C")
print(c_to_f(30))
print(f_to_c(86))