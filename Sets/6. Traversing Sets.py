# 1. Traversing using for Loop
fruits = {"apple","mango","banana"}
for fruit in fruits:
    print(fruit)

#2. Manual Counte
colors = {"Red","Pink","Yellow"}
count = 1
for color in colors:
    print(count,color)
    count += 1

# 3. Using enumerate()
animals = {"Cat", "Dog", "Lion"}
for index,animal in enumerate(animals):
    print(index,animal)

for i, value in enumerate({"A", "B", "C"}, start=1):
    print(i, value)

# 4. Traversing in Sorted Order --> ascending order
numbers = {30, 10, 20}
for x in sorted(numbers):
    print(x)

# descending order
for x in sorted(numbers, reverse=True):
    print(x)

# Modifying While Iterating
numbers = {1,2,3,4,5}
# for value in numbers:
#     if value % 2 == 0:
#         numbers.remove(value)
# print(numbers) --> runtime error because python expected that
# iterator must be same during traversal

# safe way 1
numbers = {1,2,3,4,5}
for value in numbers.copy():
    if value % 2 == 0:
        numbers.remove(value)
print(numbers)

# safe way 2
odd = set()
for i in numbers:
    if  i % 2 != 0:
        odd.add(i)
print(odd)

# safe way 3 - set comprehension
numbers = {1,2,3,4}
numbers = {x for x in numbers if x % 2 != 0}
print(numbers)

# Print all elements of a set using a for loop.
ele = {1,2,3,4,5}
for i in ele:
    print(i)

#Print elements with numbering using a manual counter.
name = {"jai","sakshi","kundan"}
count = 1
for i in name:
    print(count,i)
    count += 1

# Use enumerate() to print iteration numbers.
marks = {35,56,86,34,75}
for index,value in enumerate(marks):
    print(index,value)

# Print all elements in ascending order.
for i in sorted(marks):
    print(i)

# Print all elements in descending order.
for i in sorted(marks,reverse=True):
    print(i)

# Count how many even numbers are present in a set.
even = set(range(1,11))
for i in even.copy():
    if i%2 != 0:
        even.remove(i)
print(even)

# Print only strings with length greater than 5.
name = {"jai","sakshi","kundan"}
for i in name:
    if len(i) > 5:
        print(i)

# Remove all odd numbers safely while iterating.

remove_odd = set(range(1,11))
for i in remove_odd.copy():
    if i%2 != 0:
        remove_odd.remove(i)
print(remove_odd)

