# Frequency Counter
nums = [10, 20, 10, 30, 20, 10]
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
#
# print(freq)

# Character Frequency
text = "banana"
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# print(freq)

# Word Frequency
sentence = "python is easy python is powerful"
words = sentence.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# print(freq)

# Reverse Lookup
marks = {
    "Rahul":90,
    "Amit":80,
    "Neha":95
}
target = 80
for name, mark in marks.items():
    if mark == target:
        pass
        # print(name)

# merge two dictionary manually
d1 = {
    "A":1,
    "B":2
}
d2 = {
    "B":20,
    "C":30
}
result = d1.copy()
for key,value in d2.items():
    result[key] = value
# print(result)

# grouping data
data = [
    ("Rahul","IT"),
    ("Amit","HR"),
    ("Neha","IT"),
    ("Kiran","HR")
]

group = {}
for name, dept in data:
    if dept not in group:
        group[dept] = []
    group[dept].append(name)
# print(group)

# Invert Dictionary
student = {
    "Rahul":90,
    "Amit":80,
    "Neha":95
}
inverse = {}
for key,value in student.items():
    inverse[value] = key
# print(inverse)

# Find Duplicate Values
data = {
    "A":1,
    "B":2,
    "C":1,
    "D":3,
    "E":2
}
seen = {}
duplicate = []

for value in data.values():
    if value in seen:
        duplicate.append(value)
    else:
        seen[value] = True
# print(duplicate)

# Sort Dictionary by Key
student = {
    "city":"Pune",
    "name":"Rahul",
    "age":20
}
for key in sorted(student):
    pass
    # print(key,student[key])

#Sort Dictionary by Value
marks = {
    "Rahul":90,
    "Amit":70,
    "Neha":95
}
for key,value in sorted(marks.items()):
    pass
    # print(key,value)

# Find Maximum Value Manually
marks = {
    "Rahul":90,
    "Amit":70,
    "Neha":95
}
max_marks = None
max_student = None
# for name,marks in marks.items():
#     if marks > max_marks:
#         max_marks = marks
#         max_student = name
# print(max_student,max_marks)

# Find Minimum Value Manually
marks = {
    "Rahul":90,
    "Amit":70,
    "Neha":95
}
min_student = None
min_marks = None
for name, mark in marks.items():
    if min_marks is None or mark < min_marks:
        min_marks = mark
        min_student = name
# print(min_student, min_marks)

# List ke har element ki frequency count karo.
num = [1,2,3,4,2,5,1,3,1,3,5]
freq = {}
for nums in num:
    if nums in freq:
        freq[nums] += 1
    else:
        freq[nums] = 1
# print(freq)

# String ke har character ki frequency count karo.
text = "banana"
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
# print(freq)

# Sentence ke har word ki frequency count karo.
sentence = "python is powerful python is popular"
text = sentence.split()
freq = {}
for words in text:
    if words in freq:
        freq[words] += 1
    else:
        freq[words] = 1
# print(freq)

# Dictionary ke keys alphabetically print karo
