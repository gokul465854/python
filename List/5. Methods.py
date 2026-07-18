# append() method to add element into the list
from enum import unique

num = [1,23,45,6,4]
print(num.append(5)) # append() return None value
print(num)

# String add into the list
fruits = ["Apple","Banana","Mango"]
fruits.append("Tomato")
print(fruits)

# element add into the mixed data list
mixed = [2,"Jai",2.34]
mixed.append(True)
print(mixed)

# Add list into the exiting list
original = ["Apple","Banana","Mango"]
original.append([1,23,45,6,4])
print(original)

# adding elements using loop with user input
# a = []
# for i in range(5):
#     # n = int(input("enter a element: "))
#     # a.append(n)
# print(a)


# ----------------------extend() method----------------

numbers = [2,4,35,6]
numbers.extend([2,1,2,4])
print(numbers)

user_input1 = []
user_input2 = []

# for i in range(4):
#     a = int(input("Enter a element: "))
#     user_input1.append(a)
#     b = int(input("Enter b element: "))
#     user_input2.append(b)
# user_input1.extend(user_input2)
# print(user_input1)

# ---------------------------------insert() method -----------------------------

num = [1,2,34,5,6]
num.insert(1,89)
print(num)

# insert at middle
middle = len(num) // 2
num.insert(middle,100)
print(num)

# ----------------------------------remove() method-------------------------------
# remove first element
l = [1,2,3,4,5,2,2]
l.remove(l[0])
print(l)

# remove last element
l.remove(l[-1])
print(l)

# remove value if it exists
if 500 in l:
    l.remove(500)
# print(l)

# remove all occurrences of 2
while 2 in l:
    l.remove(2)
# print(l)

# remove duplicate values one by one
result = []
for num in l:
    if num not in result:
        result.append(num)
print(result)

# count how many times value appeared before removing
num_list = [1,2,3,4,5,2,6,9,2]
count = 0
unique = []
for num in num_list:
    if num not in unique:
        unique.append(num)
    else:
       count = count + 1
print("count: ", count)
print(unique)

# --------------------------------------------pop() method---------------------------------

# remove first element
num_list = [1,2,3,4,5,2,6,9,2]
num_list.pop(0)
print(num_list)

# remove last element
remove = num_list.pop(-1)
print(remove) # store pop element
print(num_list)

# pop all element one by one
# while num_list:
#     num_list.pop()
# print(num_list)

# reverse a list using only pop()
# reverse = []
# while len(num_list) > 0:
#     reverse.append(num_list.pop())
# print(reverse)

# remove alternative element using pop()
print(num_list)
i = 1
while i < len(num_list):
    num_list.pop(i)
    i += 1
print(num_list)

# Implementation stack using append() and pop() method
stack = []

# for i in range(1,6):
#     n = int(input("Enter a stack element: "))
#     stack.append(n)
# print("Stack: ", stack)
#
# item = stack.pop()
# print("Popped item: ", item)
# print("Stack: ", stack)

# ------------------------------------clear() method and del keyword------------------------------------
# clear list
integer_list = [1,2,3,4,5]
# integer_list.clear()
# print(integer_list)

# delete first element
print(integer_list)
del integer_list[0]
print(integer_list)

# delete last element
del integer_list[-1]
print(integer_list)

# delete alternative element
del integer_list[::2]
print(integer_list)

# ------------------------------------count(), index(), in and not in----------------------------------------
# find index of 50
marks = [10,20,30,40,50,60,10,10]
print(marks.index(50))

# count occurrences of 10
print(marks.count(10))

# check if 100 exits.
print(100 in marks)
# check 'python' exits or not
print('python' in marks)

# print 'fount' if value exits
if 30 in marks:
    print('found')
else:
    print('Not found')

# find first occurrences after 5 index
print(marks.index(10,5))

# Find Frequency of User Input
# value = int(input("enter value: "))
# frequency = marks.count(value)
# print(value, "appeared",frequency,"times")

# print all indices of 10
for i in range(len(marks)):
    if marks[i] == 10:
        print(i)