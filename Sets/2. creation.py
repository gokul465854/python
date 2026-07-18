# empty set
from statistics import stdev

data  = set()
print(data)

# Set from String
word = "banana"
letters = set(word)
print(letters)

# Set from Dictionary
student = {
    "name":"Rahul",
    "age":20,
    "city":"Pune"
}
print(set(student.items()))

# Set from Range
numbers = set(range(1,6))
print(numbers)

# set from generator
gen = (x*x for x in range(5))
s = set(gen)
print(s)

# mixed data
data = {
    10,
    3.5,
    "Python",
    True,
    (1,2)
}
print(data)

# Predict the output without running the code:
print(type({}))
print(type(set()))
print(set("hello"))
print(set({"x": 1, "y": 2}))
print({True, 1, False, 0})
print(set((1, 2, 2, 3)))