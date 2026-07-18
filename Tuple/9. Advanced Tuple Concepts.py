# Tuple Immutability (Deep Dive)
t = (1,2,3,4)
# t[0] = 5 typeError because tuple is immutable
# print(t)

t = ([1,2],[3,4])
t[0].append(3)
# print(t)
# tuple immutable hai but list nahi
# memory :
# Tuple
# +---------+
# |   ●     | -----> [1,2]
# |   ●     | -----> [3,4]
# +---------+
# tuple stored list references, reference change nahi huaa ..list object modify huyi

# tuple as dictionary key
student = {
    (101,"math") : 95,
    (101,"science") : 78
}
# print(student[(101,"math")])

# namedtuple
from collections import namedtuple
Student = namedtuple("Student",["id","name","marks"])
s = Student(20,"jai",89)
# print(s.id,s.name,s.marks)

# Tuple vs List (Memory)
import sys
t = (1,2,3)
l = [1,2,3]
print(sys.getsizeof(t))
print(sys.getsizeof(l))

# Q1. create tuple as dictionary key
contact = {
    (73,"Jai") : 7397996275,
    (98,"Sakshi") : 9823573287,
    (75,"Kundan") : 7587230898
}
# print(contact[(73,"Jai")])
# print(contact[(98,"Sakshi")])
# print(contact[(75,"Kundan")])