# ============================= any()===============
# any() check karta hai ki iterable me kam se kam ek element True hai ya nahi.
import numbers
from doctest import Example

num = [0,4,0,0]
print(any(num))

# Truthy aur Falsy
# Python me ye values False mani jati hain:
# False
# 0
# 0.0
# ''
# []
# {}
# set()
# None
# Baaki almost sab values True hoti hain.

# Exmple 2
a = ['',0,False,0.0]
print(any(a)) #--> False

# all() tabhi True return karta hai jab iterable ke sabhi elements truthy hon.
# Example 1
b = [1,2,3,4]
print(all(b)) #--> True
# Example 2
c = [0,23,4,2]
print(all(c)) #--> False
# Example 3
d = []
print(all(d)) #--> True,
# why it is true , Kyuki empty iterable me koi bhi false element nahi hai.
# Is concept ko Vacuous Truth kehte hain

# zip() --> Multiple iterables ko pair bana kar ek sath traverse karta hai.
# Example 1
name = ["Jai","Kundan","Sakshi"]
marks = [67,86,89]
for name, marks in zip(name,marks):
    pass
    # print(name,marks)
# Example 2
l1 = [1,2,3,4]
l2 = ["Jai","Sakshi"]
result = [value for value in zip(l1,l2)]
# print(result)
# zip() hamesha shortest iterable tak hi chalta hai.

# map() Har element par same function apply karta hai.
# syntax --> map(function, iterable)
# Example 1
numbers = [1,2,3,4]
result1 = map(lambda x: x*x,numbers)
# print(list(result1))

# Example 2
name_list = ["jai","sakshi","kundan"]
# print(list(map(str.upper,name_list)))

# filter() --> Condition ke basis par elements select karta hai.
# syntax --> filter(function, iterable)
# Example 1
num_list = [1,2,3,4]
result3 = list(filter(lambda x: x%2==0,num_list))
# print(result3)

# practice - easy
# Q1.Check if any number is positive.
a = [-2,-4,-9,3]
res = any(num > 0 for num in a)
# print(res)

# Q2.Check if all marks are passing
marks = [45,87,54,90]
res1 = all(mark > 40 for mark in marks)
# print(res1)

# Q3.Print names with index using enumerate()
student = ["jai","sakshi","kundan"]
# for index, value in enumerate(student):
#     print(index,value)

# Q4.merge two list using zip()
student_name = ["jai","sakshi","kundan"]
roll_NO = [1,2,3]
merge = list(zip(student_name,roll_NO))
# print(merge)

# Q5.Convert names to uppercase using map()
student_name = ["jai","sakshi","kundan"]
upper = list(map(str.upper,student_name))
# print(upper)

# medium
# Q6.Square all numbers using map().
squares = [1,2,3,4]
r = list(map(lambda x: x*x,squares))
# print(r)

# Q7.filter odd number
num = [1,2,3,4,5]
fil = list(filter(lambda x: x%2!=0,num))
# print(fil)

# Q8.Filter strings having length greater than
num = ["jai","sakshi","kundan"]
filt = list(filter(lambda x: len(x) > 5,num))
# print(filt)

# Q9.Zip three lists together
l1 = [1,2,3,4,5]
l2 = ["jai","sakshi","kundan"]
l3 = [True,False]
meger_list = list(zip(l1,l2,l3))
print(meger_list)