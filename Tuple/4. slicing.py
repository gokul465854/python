numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])

# syntax --> tuple[start : stop : step]
print(numbers[:3])
print(numbers[2:])
print(numbers[:]) # copy of tuple

numbers = (10,20,30,40,50,60)
print(numbers[0:6:2])
# every third element
print(numbers[::3])
# odd position element
print(numbers[1::2])

# reverse tuple
numbers = (10,20,30,40)
print(numbers[::-1])

# reverse alternative
print(numbers[::-2])

# negative slicing
numbers = (10,20,30,40,50)
print(numbers[-4:-1])