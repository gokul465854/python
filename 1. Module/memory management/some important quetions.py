# # Level 1 (Basic)
# # Q1.
# #
# # Output predict karo:
#
a = 10
b = 10
#
print(a == b)
print(a is b)
#
# # Q2.
# # Output predict karo:

a = [10, 20]
b = [10, 20]

print(a == b)
print(a is b)
#
# # Q3.
# # Difference batao:
#
# ==
# is

# # Ek sentence me explain karo.
# # Q4.
# # id() function kya return karta hai?
#
# Q5.
#
# Python me actual object kahan store hota hai?
#
# Stack
# Heap
#
# Aur variable kya store karta hai?
#
# 🟡 Level 2 (Intermediate)
# Q6.
#
# Output predict karo:
#
a = [1, 2]
b = a

print(a is b)
print(a == b)
# Q7.
#
# Output predict karo:
#
a = [1, 2]
b = a

b.append(3)

print(a)
print(b)
# Q8.
#
# Output predict karo:
#
a = [1, 2]
b = a.copy()

b.append(3)

print(a)
print(b)
# Q9.
#
# Memory diagram banao:
#
a = [10]
b = a
c = a

# Kitne objects bane?
# Reference count kitna hai?
#
# Q10.
#
# Ye mutable hai ya immutable?
#
# list
# tuple
# set
# dict
# int
# str
# bool
# float
# 🔴 Level 3 (Advanced)
# Q11.
#
# Output predict karo:
#
a = [10]
b = a

a = [20]

print(b)
# Q12.
#
# Output predict karo:
#
a = [1]
b = a

a.append(2)

a = [5]

print(b)
# Q13.
#
# Output predict karo:
#
a = {"x": 10}
b = a

b["y"] = 20

print(a)
# Q14.
#
# Output predict karo:
#
a = [1, 2]
b = a

print(id(a))
print(id(b))

a.append(3)

print(id(a))
print(id(b))
#
# IDs same rahenge ya change honge? Kyu?
#
# Q15.
#
# Output predict karo:
#
a = 10

print(id(a))

a = 20

print(id(a))

# ID change hogi ya nahi? Kyu?