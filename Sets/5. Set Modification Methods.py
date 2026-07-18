# 1. Add()
# Add "Python" to an empty set.
empty = set()
empty.add("python")
print(empty)

# 2. update()
# Add numbers 10, 20, 30 using update().
empty.update([10,20,30])
print(empty)

# 3. remove()
# Remove 20 using remove().
empty.remove(20)
print(empty)

# 4. discart()
# Remove 50 using discard()
empty.discard(80)
print(empty)

# 5. clear()
# Empty a set using clear()
empty.clear()
print(empty)

# Show the difference between add("ABC") and update("ABC").
empty.add("ABC")
print(empty)
empty2 = set()
empty2.update("ABC")
print(empty2)

# 6. copy()
# Copy a set and prove both have different IDs
s1 = {1,2,3,4,5}
s2 = s1.copy()
print(id(s1))
print(id(s2))
print(id(s1) is id(s2))

# 7. del
del s1
# delete the variable
# print(s1)

# Without running the code, predict the output or error:
s = {1, 2}

s.update((3, 4))
s.add(5)
s.discard(10)
s.remove(2)

print(s)

x = s.pop()

print(x)
print(s)