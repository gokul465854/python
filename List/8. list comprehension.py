# Syntax :  new_list = [expression for item in iterable]
# Yeha:
# 1. expression → Jo value list me store hogi.
# 2. item → Har iteration ka element.
# 3. iterable → List, tuple, string, range, etc.

# Example 1
numbers = [x for x in range(5)]
print(numbers)

# Example 2 - squares
l = [i*i for i in range(5)]
print(l)

# Example 3 - cubes
cube = [a**3 for a in range(5)]
print(cube)

# Example 4 - adding value in exiting list elements
m = [b+5 for b in range(5)]
print(m)

# Example 5 - String
word = "python"
letter = [ch for ch in word]
print(letter)

# Exmaple 6 - Uppercase
letter = [ch.upper() for ch in word]
print(letter)

# Example 7 - length
fruits = ["Apple", "Banana", "Mango"]
length = [len(fruit) for fruit in fruits ]
print(length)

# List Comprehension with if
# Syntax: new_list = [expression for item in iterable if condition]
# Example 1 - Even
even = [i for i in range(1,11) if i%2==0]
print(even)

# Example 2 - name start with 'A'
names = ["Amit","Rahul","Ajay","Neha"]
upper = [name for name in names if name.startswith("A")]
print(upper)

# Example 3 - nested list
matrix = [
    [1,2],
    [3,4]
]
result = [values for row in matrix for values in row]
print(result)

# print 5 table
num = 5
table = [num*i for i in range(1,11)]
print(table)