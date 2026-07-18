d = {
    "A": 1,
    "B": 2,
    "C": 3
}

# print keys or key()
# for key in d.keys():
#     print(key)
#
# # print() values using values()
# for val in d.values():
#     # print(val)

# Traversing key value pair
# for key,value in d.items():
#     print(key,value)

# using enumerate()
# for i,(key,val) in enumerate(d.items()):
#     print(i,key,val)

# sorted() for ascending order
# for i in sorted(d):
#     print(i,d[i])

# for descending order
# for i in sorted(d,reverse=True):
#     print(i,d[i])

# reverse traversal
# for key in reversed(list(d.keys())):
#     print(key,d[key])

# nested dictionary traversal
person = {
    "jai": {"age": 22, "marks": 78},
    "sakshi": {"age": 20, "marks": 89}
}
# for name, info in person.items():
#     print("Name:",name)
#     for key,val in info.items():
#         print(" ",key,":",val)

# print keys of dictionary
d = {
    "A": 1,
    "B": 2,
    "C": 3
}
# for key in d.keys():
#     print(key)

# print the value of dictionary
# for value in d.values():
#     print(value)

# key and value together
# for key,value in d.items():
#     print(key,value)

# using enumerate()
# for i,(key,value) in enumerate(d.items(), start=1):
#     print(i,key,value)

# print dictionary in alphabetical order
a = {
    "C": 3,
    "B": 2,
    "A": 1
}
# for i in sorted(a):
#     print(i,a[i])

# for i in sorted(a,reverse=True):
#     print(i,a[i])

# find sum of all dictionary values
sum = 0
for value in d.values():
    sum += value
# print(sum)

# print only even value
for value in d.values():
    if value % 2 == 0:
        pass
      # print(value)

# print the student who have above 90 marks
student = {
    "Jai": 89,
    "Sakshi":  98,
    "Kundan":92
}
for name, marks in student.items():
    if marks > 90:
        pass
        # print(name,marks)


# print the student information in nested dictionary
student = {
    "Jai": {"subject": "math","marks": 89},
    "Sakshi": {"subject": "math","marks": 98},
    "Kundan": {"subject": "math", "marks": 94}
}
for key, value in student.items():
    pass
    # print(key,value["marks"])

# find maximum and minimum using loop
data = {
    'a': 10,
    'b': 24,
    'c': 78,
    'd': 69,
    'e': 89
}

# max
max = data['a']
for value in data.values():
    if value > max:
        max = value

# min
min = data['a']
for value in data.values():
    if value < min:
        min = value

print(f"max: {max}, min: {min}")