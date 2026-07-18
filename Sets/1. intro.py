# 1. Collection
# multiple values stored in the single variable
from traceback import print_tb

numbers = {10,20,30}
print(numbers)
print(type(numbers))

# 2. Unique
# duplicate values removed automatically
unique = {1,2,3,4,5,1,2,3,4,5}
print(unique)

# 3. Unordered
unordered = {1,2,3,4,5}
# print(numbers[1]) --> error because set is unordered,
# values are not accessing using index

# 4. Mutable
mutable = {1,2,3,4,5}
# set allowed to modify its values
mutable.add(6)
print(mutable)

# 5. Hashable Objects
# stored only hashable object - immutable objects
# 10
# 3.5
# True
# "python"
# (1,2)
# frozenset({1,2})

# create empty set
empty_set = set({})
print(empty_set)

# Create a set containing five integers.
integers = {1,2,3,4,5}
print(integers)

# Create a set from a list with duplicates.
duplicate = [1,2,4,2,3,1]
print(set(duplicate))

# Print the type of {} and set().
print(type({}))
print(type(set({})))

# Check whether 50 exists in a set.
check = {10,20,30,40,50}
if 50 in check:
    print("yes")

# Print all elements using a for loop.
elements = {1,2,3,4,5}
for i in elements:
    print(i)

# Remove duplicates from a list using a set.
t = {("jai",67),
     ("sakshi",90),
     ("kundan",56)}
print(t)
print(type(t))
