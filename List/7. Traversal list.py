# using for loop
a = [10,20,30,40]
# for i in a:
# # print(i)

# using range()
# for i in range(len(a)):
#     print(i,a[i])

# using enumerate()
# for index, value in enumerate(a):
#     print(index,value)

# using while loop
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# reverse traversal method 1
# for i in reversed(a):
#     print(i)

# method 2
# for i in a[::-1]:
#     print(i)

# Nested list traversal
# matrix = [
#     [1,2],
#     [3,4],
#     [5,6]
# ]
# for row in matrix:
#     for value in row:
#         print(value)

# # print even index element
# l = [100,200,300,500,800]
# for index,value in enumerate(l):
#     if index % 2 == 0:
#         print(index, value)

# print reverse alternative element
# for i,value in enumerate(reversed(l)):
#     if i % 2 != 0:
#         print(value)

# Traverse nested list
# matrix_list = [
#     [1,2],
#     [3,4],
#     [5,6]
# ]
# for row in matrix_list:
#     for value in row:
#         print(value)

# raverse two lists together using zip().
a = [1,2,3]
# b = ["apple","banana","mango"]
# for i in zip(a,b):
#     print(i)

# Traverse with enumerate(start=100).
# for index,value in enumerate(a,start=100):
#     print(index,value)

#===================== Hard quetions ===============
# Print matrix row-wise
# matrix = [
#     [1,2],
#     [3,4],
#     [5,6]
# ]
#
# for row in matrix:
#     for value in row:
#         print(value,end =" ")
#     print()


# column wise
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# rows = len(matrix)
# cols = len(matrix[0])

# for j in range(cols):
#     for i in range(rows):
#         print(matrix[i][j], end=" ")
#     print()

# Print all elements of the first row
# print(matrix[0])
# print(matrix[-1])

# print sum of all rows
# for rows in matrix:
#     print(sum(rows))

# or
# for rows in matrix:
#     sum = 0
#     for element in rows:
#         sum += element
#     print(sum)

# Find the maximum element in each column
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for rows in matrix:
    max = 0
    for element in rows:
        if max < element:
            max = element
    # print(max)

# Count even numbers in every column.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for rows in matrix:
    count = 0
    for element in rows:
        if element % 2 == 0:
            count += 1
    # print(count)

# Print columns in reverse order (last to first)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rows = len(matrix)
cols = len(matrix[0])

for j in range(cols - 1, -1, -1):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()

