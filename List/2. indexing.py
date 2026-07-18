# print first element using indexing
from _testcapi import MyList

l = list(range(11))
print(l[0])

# print last element
print(l[-1])

# print second element
print(l[1])

# print second last element
print(l[-2])

# print length of list
print(len(l))

# print middle element of list
middle = (l[0] + l[-1]) / 2
print(middle)

# print last element using len()
print(l[len(l) - 1])

# accessing nested list element
nested = [[1,2],[3,4]]
print(nested[0][1])

# Create a list and print every element using its index
my_list = list(range(6))
for index in range(len(my_list)):
    print(f"{index}")

data = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(data[2][1])
print(data[-1][-2])
print(data[-3][-1])