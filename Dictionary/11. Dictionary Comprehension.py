squares = {i: i*i for i in range(1,6)}
print(squares)

# using list - count the length of sting
names = ["apple","banana","mango"]

d = {name: len(name) for name in names}
print(d)

# using tuple
t = (10,20,30,40)
d = {i: i // 10 for i in t}
print(d)

# using string
str = "python"
d = {ch: ord(ch) for ch in str}
print(d)

# using if
squares = {
    x: x*x
    for x in range(1,11)
    if x % 2 == 0
}
print(squares)

# using if else
num = {x: "Even" if x%2 == 0 else "Odd" for x in range(1,11)}
print(num)

# Swapping Keys & Values
student = {
    "Rahul":90,
    "Amit":80,
    "Neha":95,
    "jai": 90
}
newD = {value: key for key,value in student.items()}
print(newD)

# convert list into dictionary
names = ["A", "B", "C"]
d = {
    name: 0
    for name in names
}
print(d)

# Dictionary from Two Lists
name = ["Jai","Sakshi","Kundan"]
marks = [76,89,98]

d = {name: marks for name,marks in zip(name,marks)}
print(d)

# Nested Dictionary Comprehension
student = {
    name: {
        "marks":78
    }
    for name in ["rahul","amit"]
}
print(student)

# Employee salary after 10% increment
salary = {
    "Rahul":50000,
    "Amit":40000,
    "Neha":60000
}
new_salary = {emp: sal * 1.10 for emp,sal in salary.items()}
print(new_salary)

# Sirf even numbers ka square dictionary bana
even = {x: x*x for x in range(1,11) if x%2 == 0}
print(even)

# Marks dictionary me 90+ marks wale students filter karo
marks = {
    "jai": 89,
    "sakshi": 91,
    "kundan": 96
}
new = {key: value for key,value in marks.items() if value > 90}
print(new)

# Dictionary ke keys aur values swap karo
marks = {
    "jai": 89,
    "sakshi": 91,
    "kundan": 96
}
newD = {value: key for key,value in marks.items()}
print(newD)

# Salary me 20% increment karke nayi dictionary banao
salary = {
    "jai": 70000,
    "sakshi": 50000,
    "kundan": 60000
}
new_sal = {key: value * 1.20 for key,value in salary.items()}
print(new_sal)