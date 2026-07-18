# addition of two matrix

A = [
    [1, 2],
    [3, 4]
]
B = [
    [5, 6],
    [7, 8]
]
result = []
for i in range(len(A)):
    c = []
    for j in range(len(A[0])):
        c.append(A[i][j] + B[i][j])
    result.append(c)
# print(result)

# matrix subtraction
A = [
    [1, 2],
    [3, 4]
]
B = [
    [5, 6],
    [7, 8]
]
res = []
for i in range(len(A)):
    c = []
    for j in range(len(A[0])):
        c.append(B[i][j] - A[i][j])
    res.append(c)
# print(res)

# Transpose matrix
a = [
    [1,2,3],
    [4,5,6]
]
result = []
for j in range(len(a[0])):
    b = []
    for i in range(len(a)):
        b.append(a[i][j])
    result.append(b)
print(result,end=" ")

# print upper triangular matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if j>=i:
            pass
            # print(matrix[i][j], end=" ")
        else:
            pass
            # print(" ",end=" ")
    # print()

# Print lower triangular matrix.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row = len(matrix)
cols = len(matrix[0])
for i in range(row):
    for j in range(cols):
        if i>j or i==j:
            pass
            # print(matrix[i][j],end=" ")
        else:
            pass
            # print(" ",end=" ")
    # print()

# check if matrix is symmetric
matrix = [
    [1,2,3],
    [2,5,6],
    [3,6,9]
]
is_symmetric = True
n = len(matrix)

for i in range(n):
  for j in range(i + 1, n):
    if matrix[i][j] != matrix[j][i]:
      is_symmetric = False
      break
  if not is_symmetric:
    break

if is_symmetric:
  print("It is symmetric")
else:
  print("Not symmteric")

# Multiply two matrices.
a = [
    [1, 2],
    [3, 4]
]
b = [
    [5, 6],
    [7, 8]
]
multi = []

row = len(a)
cols = len(b[0])
common = len(b)

for i in range(row):
    c = []
    for j in range(cols):
        total = 0
        for k in range(common):
            total += a[i][k] * b[k][j]
        c.append(total)
    multi.append(c)
for r in multi:
    pass
    # print(r)

# Find sum of primary diagonal.
matrix = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]
row = len(matrix)
cols = len(matrix[0])
sum = 0
for i in range(row):
    for j in range(cols):
        if i == j:
            sum += matrix[i][j]
# print(sum)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row = len(matrix)
cols = len(matrix[0])
sum2 = 0
for i in range(row):
    for j in range(cols):
        if i + j == len(matrix) - 1:
            sum2 += matrix[i][j]
# print(sum2)

# print matrix in zig zag order
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(matrix)):
    if i%2 == 0:
        for j in range(len(matrix[0])):
            pass
        #     print(matrix[i][j],end=" ")
        # print()
    else:
        for j in range(len(matrix) - 1, - 1, - 1):
            pass
        #     print(matrix[i][j],end=" ")
        # print()

# Rotate matrix 90 clockwise
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Transpose
for i in range(len(matrix)):
    for j in range(i,len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# reverse
for row in matrix:
    row.reverse()
for row in matrix:
    pass
    # print(row)

# find the largest element in each row
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    max = row[0]
    for num in row:
        if num > max:
            max = num
    # print(max)

#count even and odd element in matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
even = 0
odd = 0
for row in matrix:
    for num in row:
        if num%2 == 0:
            even +=1
        else:
            odd += 1
print("even: ",even, " ", "odd: ",odd)