# A hash ek integer number hota hai jo kisi
# object ki identity/value ko represent karta hai.
print(hash(10))

print(hash("python"))

print(hash((1,2)))

# Without running the code, predict the output or error:
print(hash("python"))

print(hash((1, 2, 3)))

print({True, 1, 2})

print(hash((1, (2, 3))))

# print(hash((1, [2, 3]))) --> TypeError: unhashable type: 'list'

print({False, 0, True, 1})