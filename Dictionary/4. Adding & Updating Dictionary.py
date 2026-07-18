# update()
student = {
    "name": "Rahul",
    "age": 20
}

student.update({
    "age": 25,
    "city": "Delhi"
})

print(student)

# update() with List of Tuples
d = {
    "A": 1
}

d.update([
    ("B", 2),
    ("C",3)
])
print(d)

# update() with Keyword Arguments
d.update(D=4,E=5)
print(d)

# setdefault()
student = {
    "name": "Rahul"
}
print(student.setdefault("name", "Amit"))
print(student)

# nested dictionary update
student = {
    "name": "Rahul",
    "address": {
        "city": "Pune"
    }
}
student["address"]["city"] = "jabalpur"
student["address"]["state"] = "maharastra"
print(student)

# merge two dictionary
d1 = {
    "A": 1,
    "B": 2
}
d2 = {
    "B": 20,
    "C": 30
}
d3 = d1 | d2
print(d3)

# Merge Using |=
d3 = {
    "A": 1,
    "B": 2
}

d3 |={
    "B": 20,
    "C": 30
}
print(d3)

# merge using update
d1 = {
    "A": 1
}
d2 = {
    "B": 2
}
d1.update(d2)
print(d1)