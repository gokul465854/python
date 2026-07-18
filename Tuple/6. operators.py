# Concatenation Operator (+)
t1 = (1,2,3,4,5)
t2 = (6,7,8,9)
result = t1 + t2
# print(result)

# Repetition Operator (*)
t = (1,2)
# print(t * 3)

color = ("red","pink")
# print(color * 5)

# Membership Operator (in)
t = (10,20,40,50)
# print(30 in t)
# print(20 in t)

# and (not in)
t = (1,2,3,4,5)
# print(8 not in t)
# print(2 not in t)

# Equality Operator (==)
t1 = (1,2,3,4,5)
t2 = (1,2,3,4,5)
# print(t1 == t2)

# Not Equal (!=)
t1 =(1,2)
t2 =(3,4)
# print(t1 != t2)

# Lexicographical Comparison
# print((10,20) < (10,30))
# print((30,100) > (10,1000))
# print((2,) >= (2,0))
# print((2,) <= (3,))
print(() < ()) # False
print(() <= ()) # True
print((True,) > (False,))
print((True,) <= (False,))
print((1,2) <= (1,2,0))
print((0,) >= (0,))