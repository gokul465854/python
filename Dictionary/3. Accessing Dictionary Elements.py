from statistics import stdev

student = {
    "name": "Rahul",
    "age": 20
}

print(student["name"])

d = {
    1: "One",
    2: "Two",
    3: "Three"
}

print(d[2])

student = {
    "name": "Rahul",
    "address": {
        "city": "Pune",
        "state": "Maharashtra"
    }
}

print(student["address"])
print(student["address"]["city"])

# Accessing List Inside Dictionary
student = {
    "marks": [90, 80, 95]
}

print(student["marks"])
print(student["marks"][1])

# Using get()
student = {
    "name": "Rahul"
}
print(student.get("name"))
print(student.get("age"))
print(student.get("age",0))

# keys()
student = {
    "name": "Rahul",
    "age": 20,
    "city": "Pune"
}

print(student.keys())
print(student.values())
print(student.items())

# Membership Testing
# Dictionary me in aur not in keys ko check karte hain
student = {
    "name": "Rahul",
    "age": 20,
    "city": "Pune"
}
print("name" in student)
print("marks" in student)

# update()
student = {
    "name": "Rahul",
    "age": 20
}

student.update({
    "city": "Pune",
    "marks": 90
})

print(student)