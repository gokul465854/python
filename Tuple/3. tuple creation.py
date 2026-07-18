# common method to create tuple
from asyncio import ensure_future
from functools import lru_cache

numbers = (10, 20, 30)
# print(numbers)

# Tuple Without Parentheses (Packing)
# Python automatically tuple bana deta hai
num = 10,20,30,40,50
# print(num)
# print(type(num))
# output: (10,20,30,40,50) and type <class 'tuple'>

# Creating Tuple using tuple() Constructor
# tuple() sirf iterable object ko tuple me convert karta hai.
# Examples of iterable:
# List ✅
# String ✅
# Set ✅
# Dictionary ✅ (keys)
# Range ✅
# Integer iterable nahi hota.

# list --> tuple
l = [1,2,3,4,5]
t = tuple(l)
# print(t)
# print(type(t))
# output: (1, 2, 3, 4, 5) and <class 'tuple'>

# String --> tuple
name = "Sakshi"
n = tuple(name)
# print(n)
# print(type(n))
# output: ('S', 'a', 'k', 's', 'h', 'i') and <class 'tuple'>

# Range --> Tuple
a = tuple(range(5))
# print(a)

# nested tuple
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# print(matrix)

# deep nested tuple
data = (
    10,
    (
        20,
        (
            30,
            40
        )
    )
)

# print(data)

# Q1. while loop se print karo
a = (1,2,3,4,5)
i = 0
while i < len(a):
    # print(a[i], end=" ")
    i += 1

# Q2. range() se print karo.
for i in range(len(a)):
    pass
    # print(a[i], end=" ")

# Q3. enumerate() use karo
for index,value in enumerate(a):
    pass
    # print(index,value)

# Q4. print reverse
for i in a[::-1]:
    pass
    # print(i, end=" ")

# find maximum number
max = a[0]
for i in range(len(a)):
    if max < a[i]:
        max = a[i]
# print(max)

# find square of each element of tuple
for i in a:
    pass
    # print(i ** 2, end=" ")

# count zero
count = 0
for i in range(len(a)):
    if a[i] == 0:
        count +=1
# print(count)

# print reverse alternative element
for i in range(len(a) - 1, - 1, -2):
    pass
    # print(a[i], end=" ")

# check tuple sorted or not
a = (1,2,3,4,5)
is_sorted = True
for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        is_sorted = False
        break
if is_sorted:
    pass
    # print("tuple is sorted")
else:
    print("tuple is not sorted")

# using all()
t = (10, 20, 30, 40)
if all(t[i] <= t[i + 1] for i in range(len(t) - 1)):
    pass
    # print("tuple is sorted")
else:
    print("tuple not sorted")

# check palindrome
num = [1,2,3,2,1]
is_palindrome = True
for i in range(len(num) // 2):
    if num[i] != num[len(num) - 1 - i]:
        is_palindrome = False
        break
if is_palindrome:
    pass
    # print("it is palindrome")
else:
    print("it is not palindrome")

# using slicing
if num == num[::-1]:
    pass
    # print("palindrome")
else:
    print("not palindrome")

# check descending order
l = 50,40,30,20,10
if all(l[i] > l[i+1] for i in range(len(l) - 1)):
    pass
    # print("tuple is descendin order")
else:
    print("not descending")

same = 5,5,5,5
is_same = True
for i in same:
    if i != same[0]:
        is_same = False
        break
# print(is_same)

# count the ascending order break
t = (10, 20, 15, 30, 25, 40)
count = 0
for i in range(len(t) - 1):
    if t[i] > t[i+1]:
        count += 1
# print(count)

# print first unsorted element
t = (10, 20, 15, 30, 25, 40)
found = False

for i in range(len(t) - 1):
    if t[i] > t[i+1]:
        # print("first unsorted element: ", i + 1)
        found = True
        break
if not found:
    print("tuple is sorted")

# Count mismatched pairs
t = (1, 2, 3, 4, 2, 1)

left = 0
right = len(t) - 1
count = 0

while left < right:
    if t[left] != t[right]:
        count += 1

    left += 1
    right -= 1

# print("Mismatched pairs:", count)

# Print First Mismatched Pair (Optimized)
t = (1, 2, 3, 4, 2, 1)

left = 0
right = len(t) - 1

while left < right:
    if t[left] != t[right]:
        print("First mismatched pair:", t[left], t[right])
        break

    left += 1
    right -= 1
else:
    print("No mismatched pair")