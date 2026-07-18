# tuple packing
a = 10
b = 20
c = 30

t = a,b,c
# print(t,type(t))

# tuple unpacking
t = (1,2,3,4,5)
# a,*all,b = t
# print(a)
# print(all)
# print(b)

# ignore Values (_)
t = (10,20,30)
a,_,c = t
print(a)
print(c)

# nested unpacking
t = (1,(2,3))
a,(b,c) = t
print(a)
print(b)
print(c)