# Normal vs Update methods
a = {1,2,3}
b = {2,3,4}
c = a.intersection(b)
print(a)
print(c) # a is not change

# update operation
a = {1,2,3}
b = {2,3,4}
a.intersection_update(b)
print(a) # a is modify

