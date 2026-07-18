# Traversal Using for Loop
numbers = (10, 20, 30, 40)
# for i in numbers:
#     print(i)

# Traversal using while loop
num = 10,20,30,40,50
i = 0
# while i < len(num):
#     print(num[i])
#     i += 1

# Traversal using range()
# num = 10,20,30,40,50
# for i in range(len(num)):
#     print(num[i])

# Traversal using enumerate()
num = 10,20,30,40,50
for index,value in enumerate(num):
    pass
    # print(index,value)

# reverse Traversal
# example 1
numbers = (10,20,30,40)
for num in numbers[::-1]:pass
    # print(num)

# example
numbers = (10,20,30,40)
for i in range(len(numbers) -1,-1,-1):pass
    # print(numbers[i])

# nested tuple traversal
matrix = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
for row in matrix:
    pass
    # print(row)

# find sum
num = 10,20,30,40,50
sum = 0
for i in range(len(num)):
    sum += num[i]
print(sum)

# find product
product = 1
for i in range(len(num)):
    product *= num[i]
print(product)