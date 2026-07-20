# Without comprehension
s = set()
for i in range(1,5):
    s.add(i)
print(s)

# With comprehension
s = {i for i in range(1,5)}
print(s)

# squares
sqr = {x*x for x in range(1,6)}
print(sqr)

# cube
cubes = {x ** 3 for x in range(5)}
print(cubes)

# Automatic Duplicate Remova
s = {1,1,2,2,3,4,3}
result = {x for x in s}
print(result)

# Conditional Set Comprehension
even = {x for x in range(1,11) if x%2 == 0}
print(even)

# Strings
words = ["apple", "banana", "cat"]
result = {w.upper() for w in words}
print(result)

# Multiple Loops
pair = {
    (x,y)
    for x in [1,2]
    for y in [3,4]
}
print(pair)

# nested condition
result = {
    x
    for x in range(20)
    if x % 2 == 0 and x % 3 == 0
}
print(result)

# Using Functions
num = [-5,-2,3,4]
result = [abs(x) for x in num]
print(result)

name = ["jai","sakshi","kundan"]
result = {w.capitalize() for w in name}
print(result)

# Unique Email Domains
emails = [
    "a@gmail.com",
    "b@yahoo.com",
    "c@gmail.com"
]
domain = {
    email.split("@")[1]
    for email in emails
}
print(domain)

# Unique Lengths
words = [
    "car",
    "apple",
    "dog",
    "banana"
]
len = {
    len(w)
    for w in words
}
print(len)

# Unique First Letters
worda = [
    "apple",
    "banana",
    "cat",
    "ball"
]
unique = {
    unique[0]
    for unique in worda
}
print(unique)