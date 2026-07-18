# integer tuple
numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))

# string tuple
fruits = ("Apple", "Mango", "Banana")
print(fruits)

# Boolean tuple
is_truth = (True,False)
print(is_truth)

# float tuple
decimal = (2.4,34.5,75.7,12.78)
print(decimal)

# mixed datatype tuple
mixed = (1,"Apple",True,34.78)
print(mixed)

# empty tuple
empty = ()
print(empty)

# single element tuple
single = (5)
print(single)
print(type(single))
# output: 5, <class 'int'> but why ,
# because python me single element ko integer samjhta hai
# tuple me coma zaruri hota hai --> (5,) tab iska type <class 'tuple'>   aayega
singel2 = (5,)
print(singel2)
print(type(singel2))
# output: (5,) and type <class 'tuple'>

# Allow duplicate values
dup = (1,2,2,3,3,4,5,6,6)
print("duplicate values: ",dup)
# tuple duplicate values ko remove nahi karta

# Kab Tuple Use Kare?
# fixed data
days = (
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun"
)
# co-ordinate
point = (10,20)
# RGB color
red = (255,0,0)
# database records
student = (
    101,
    "Amit",
    88.5
)