numbers = [10,20,30,40,50,60,70]

# print first three numbers
print(numbers[0:3])

# print last three numbers
print(numbers[2:])

# print every second element
print(numbers[1:len(numbers):2])

# reverse a list
print(numbers[::-1])

# copy the list using slicing
print(numbers[:])

# print the middle three numbers
middle = len(numbers) // 2
print(numbers[middle-1: middle+2])

# print alternative element
print(numbers[::2])

# print reverse alternative element
print(numbers[::-2])

# slicing using negative indexing
print(numbers[-7:-1])