# print main diagonal
from math import trunc

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# for i in range(len(matrix)):
#     print(matrix[i][i],end=" ")

# print secondary diagonal
# for i in range(len(matrix)):
#     print(matrix[i][len(matrix) - 1 - i],end=" ")

# print border element
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rows = len(matrix)
cols = len(matrix[0])

# for i in range(rows):
#     for j in range(cols):
#         if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
#             print(matrix[i][j], end=" ")

# Search an Element in Matrix
target = int(input("Enter number: "))
found = False
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == target:
            print("Found")
            found = True
            break
    if found:
        break
if found == False:
    print("Not found")


