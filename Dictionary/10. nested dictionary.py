from statistics import stdev

students = {
    "Rahul": {
        "age": 20,
        "marks": 90
    },
    "Amit": {
        "age": 22,
        "marks": 80
    }
}

print(students)
# update dictionary
students["Rahul"]["age"] = 22
print(students)

# add new nested key
students["Rahul"]["city"] = "pune"
print(students)

# add new student
students["Sakshi"] = {
    "age": 20,
    "city": "Jabalpur",
    "marks": 89
}
print(students)

# delete nested key
del students["Sakshi"]["city"]
print(students)

# delete complete student
del students["Sakshi"]
print(students)

# Traversing nested dictionary
for student, details in students.items():
    print(students)
    for key,value in details.items():
        print(key,value)

# searching
students = {
    "Rahul": {
        "marks": 90
    },
    "Amit": {
        "marks": 80
    }
}
if "Rahul" in students:
    print("Found")

# search nested value
print(students["Rahul"].get("marks"))

# safe searching
if "Rahul" in students:
    if "marks" in students["Rahul"]:
        print(students["Rahul"]["marks"])

# three level nested dictionary
data = {
    "class10": {
        "Jai": {
            "subject": "math",
            "marks": 89
        }
    }
}
print(data)
data["class10"]["Jai"]["marks"] = 90
print(data)

# real world example
employees = {
    101: {
        "name": "Rahul",
        "salary": 50000,
        "department": "IT"
    },
    102: {
        "name": "Amit",
        "salary": 60000,
        "department": "HR"
    }
}
for employee, details in employees.items():
    print(employee)
    for key,value in details.items():
        print(key,":",value)

# 3-level nested dictionary banao (School → Class → Student → Marks) aur traverse karo.
studentsDetails = {
    "School1": {
        "class10": {
            "jai": {
                "marks": 89
            }
        }
    }
}
print(studentsDetails["School1"]["class10"]["jai"]["marks"])

# Employee database banao aur manually highest
# salary wale employee ka naam find karo (bina max() use kiye).
employee = {
    "Amit": 45000,
    "Priya": 62000,
    "Rahul": 58000,
    "Neha": 75000,
    "Karan": 68000
}
emp_name = ""
highest_salary = -1
for name,salary in employee.items():
    if salary > highest_salary:
        highest_salary = salary
        emp_name = name
print(f"name: {emp_name} and highest salary: {highest_salary}")