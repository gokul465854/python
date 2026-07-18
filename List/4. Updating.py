numbers = [10,20,30,40,50]
print(numbers)
numbers[0] = 100
print(numbers)

# last element update
l = ["apple", "banana", "mango"]
l[-1] = "Tomato"
print(l)

# Multiple Elements Update (Slice Assignment)
num_list = [1,2,3,4,5]
num_list[1:4] = [20,30,40]
print(num_list)

# different slice size
num_list[1:4] = [100]
print(num_list)

# replace entire list
fruits = ["Apple", "Banana", "Mango","Tomato"]
print(id(fruits))
fruits[:] = [1,2,3]
print(fruits)
print(id(fruits))

# Invalid Index Update
# fruits[8] = 'Mango'
# print(fruits)
# IndexError:
# list assignment index out of range

# Nested list update
matrix = [
    [1,2],
    [3,4]
]
matrix[0][1] = 100
print(matrix)

# updating list using loop
marks = [10,20,30,40,50]
for i in range(len(marks)):
    marks[i] *= 2
print(marks)


# replace middle element
a = [2,3,5,7,8]
middle = len(a) // 2
print(len(a))
a[middle] = 30
print(a)

# replace all elements
marks2 = [1,2,3]
print(marks2)
print(id(marks2))
marks2[:] = [45,2,36,34]
print(id(marks2))
print(marks2)


# Replace first three elements using slicing
b = [34,22,34,57,89]
b[0:3] = [1,2,3]
print("Replace three element: ", b)

# Replace two element with one element
c = [1,2,3,4,5]
c[1:3] = [6]
print(c)
# replace one element with three elements
c[1:2] = [2,3,9]
print(c)