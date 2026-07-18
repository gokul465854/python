# empty dictionary
d = {}
# print(d)

# Using dict()
student = dict(name="jai",age=20,marks=78)
# print(student)

# using list of tuple
data = [
    ("name", "jai"),
    ("subject", "math"),
    ("marks",90)
]
result = dict(data)
# print(result)

# using tuple of tuples
data = (
    ("A",10),
    ("B",20),
    ("C",30)
)
d = dict(data)
# print(d)

# using zip()
name = ["Jai","Sakshi","Kundan"]
marks = [78,64,67]

student_data = dict(zip(name,marks))
# print(student_data)

# using fromkeys()
# syntax --> dict.fromkeys(keys, value)
keys = ["A","B","C"]
# d = dict.fromkeys(keys)

# fromkeys() with mutable object
d = dict.fromkeys(keys,[])
d["A"].append(100)
# print(d)

# correct way
keys = ["A","B","C"]
d = {key: [] for key in keys}
d["A"].append(100)
# print(d)

# Dictionary Comprehension
# syntax --> {
#     key: value
#     for variable in iterable
# }

numbers = [1,2,3,4,5]
squares = {x: x*x for x in numbers}
# print(squares)

# nested dictionary
students_details = {
    "Jai": {
        "subject": "math",
        "marks": 89
    },
    "Sakshi": {
        "subject": "math",
        "marks": 78
    }
}
# print(students_details)

# Dictionary from Existing Dictionary
d1 = {
    "A": 1,
    "B": 2
}
d2 = dict(d1)
print(d2)