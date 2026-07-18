students = {
    "name": "jai",
    "age" : 21,
    "city": "Chhtrapati sambhajinagar"
}
print(students)
# print(students["name"])
# print(students["age"])
# print(students["city"])
# students["name"] = "Sakshi"
# students["age"] = 20
# students["city"] = "jabalpur"
# print(students, type(students))

car = {
    "brand":"BMW",
    "price":5000000,
    "color":"Black"
}
# Dictionary Memory View
# car:
# ┌───────────────┐
# │ brand │ BMW   │
# ├───────────────┤
# │ price │5000000│
# ├───────────────┤
# │ color │ Black │
# └───────────────┘

# empty dictionary
d = {}
d["x"] = 1
d["y"] = 2
d["z"] = 3
print(d,type(d))

# allowed immutable keys examples: int, float, boolean, tuple, string
# mutable key not allowed ex: list, set,dictionary --> Agar key change ho gayi,
# to Python usse reliably find nahi kar payega. Isliye dictionary sirf hashable
# (immutable) objects ko key banane deti hai.
d2 = {
    1: "one",
    3.34: "PI",
    True: "yes",
    (1,2): "tuple"
}
# print(d2)

record = {
    "number": 10,
    "name": "Jai",
    "age": 20,
    "marks": [78,98,65],
    "address": {
        "state": "maharastra",
        "city": "chhtrapati sambhajinagar"
    },
    "set": {5,6},
    "tuple": (1,2)

}
print(record)
print(record[("address")])
print(record["marks"])