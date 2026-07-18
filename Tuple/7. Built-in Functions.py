t = (1,6,3,4,2,5)
# print(len(t))

# return the largest element
# print(max(t))

name = ("jai","sakshi","kundan")
print(max(name))
# String alphabetically compare hota hai

print(min(name))
print(sum(t))

print(sorted(t))

# descending order
print(sorted(t,reverse = True))

print(t.count(1))
print(t.index(5))

# safe way to find index
if 9 in t:
    print(t.index(9))
else:
    print("not found")

# manual index
target = 2
for i in range(len(t)):
    if t[i] == target:
        print(i)
        break

# find duplicate
t = 1,2,4,5,3,3,5,4
for i in range(len(t)):
    if t.count(i) > 1:
        pass
        # print(i)

# unique duplicate printing
t = (10,20,10,30,20)
printed = ()
for i in t:
    if t.count(i) > 1 and i not in printed:
        printed += (i,)
print(printed)