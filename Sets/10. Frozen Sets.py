# Creating a Frozenset
fs = frozenset()
print(fs)
print(type(fs))

# from list
fs = frozenset([1,2,3,4,5])
print(fs)

# from tuple
fs = frozenset((1,2,3,4,5))
print(fs)

# from string
fs = frozenset("banana")
print(fs)

# From Existing Set
a = {1,2,3,4,5}
fs = frozenset(a)
print(fs)

# Supported Operation
a = frozenset({1,2,3})
b = frozenset({3,4,5})

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

# Nested Sets
A = {
    frozenset({1, 2}),
    frozenset({3, 4})
}
print(A)

# dictionary key
# key = {
#     frozenset({1,2}): "A",
#     frozenset(3,4): "B"
# }
# print(key)

# Create an empty frozenset.
fs = frozenset()
print(fs)
# Convert a list into a frozenset.
fs = frozenset([1,2,3,4,5])
print(fs)
# Check membership using in.
fs = frozenset({1,2,3,4,5})
# print(1 in fs)
# Find the union of two frozensets.
a = frozenset({1,2,3})
b = frozenset({3,4,5})
print(a | b)
# Print the length of a frozenset
print(len(a))

# Use a frozenset as a dictionary key.
key = {
    frozenset({1,2}): "A",
    frozenset({3,4}): "B"
}
print(key)
# Create a set of frozensets.
fs = frozenset({1,2,3,4,5,6})
print(fs)
# Show that add() raises an error.
# fs.add(2) --> AttributeError: 'frozenset' object has no attribute 'add'