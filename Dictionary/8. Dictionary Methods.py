# clear()
student = {
    "A": 1,
    "B": 2,
    "C": 3
}
# print(student)
# student.clear()
# print(student)

# copy()
copyDictionary = student.copy()
# print(copyDictionary)
# print(id(student))
# print(id(copyDictionary))

# fromkeys()
keys = ["A","B","C"]
d = dict.fromkeys(keys,0)
# print(d)

# get()
print(student.get("A"))

# keys()
print(student.keys())

# pop()
x = student.pop("A")
print(x)
print(student)