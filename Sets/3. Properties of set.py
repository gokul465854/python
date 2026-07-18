a = {1, 2, 3}
b = {3, 2, 1}

print(a == b)

a.add(4)
a.add(4)

print(a)

print(len(a))

print(type(frozenset({1, 2})))
print({frozenset({1, 2}), frozenset({2, 1})})