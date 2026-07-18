# Membership Operator (in)
student = {
    "name": "Rahul",
    "age": 20,
    "city": "Pune"
}
print("name" in student)
# not in
print("marks" not in student)

# Value Searching
print(20 in student.values())

# Searching Keys
marks = {
    "Math": 90,
    "English": 80,
    "Science": 95
}

if "Math" in marks.keys():
    print("subject found")
else:
    print("not found")

# Searching Using get()
print(marks.get("Math"))

print(marks.get("history", "not found"))

# setdefault() for Searching
print(marks.setdefault("History",40))

# Searching Nested Dictionary
students = {
    "Rahul": {
        "marks": 90
    },
    "Amit": {
        "marks": 80
    }
}
# print("Rahul" in students)
# print(students["Rahul"]["marks"])

# safe way
if "Rahul" in students:
    print(students["Rahul"].get("marks"))

# Searching Every Value
marks = {
    "Rahul": 90,
    "Amit": 70,
    "Neha": 95
}
target = 85
for value in marks.values():
    if value == target:
        print("found")

# Searching Key by Value
target = 95
for key, value in marks.items():
    if target == value:
        print(key)

# Multiple Keys Search
info = {
    "name": "Rahul",
    "age": 20,
    "city": "Pune"
}
required = ["name","city"]
for key in required:
    if key in info.keys():
        pass
        # print(key,"found")
print(all(key in info for key in required))
