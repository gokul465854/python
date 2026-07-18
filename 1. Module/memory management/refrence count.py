# ============================================================
# PYTHON REFERENCE COUNT - COMPLETE NOTES
# ============================================================

# ------------------------------------------------------------
# What is Reference Count?
# ------------------------------------------------------------
# Reference Count tells how many variables are referring
# (pointing) to the same object.
#
# Simple Definition:
# "Reference Count = Number of references (variables)
# pointing to the same object."
# ------------------------------------------------------------


# ============================================================
# Example 1
# ============================================================

a = [10, 20]

# Memory:
#
# a  --------->  [10, 20]
#
# Reference Count = 1
#
# Because only variable 'a' is pointing to this list.


# ============================================================
# Example 2
# ============================================================

a = [10, 20]
b = a

# Memory:
#
# a ----\
#        \
#         -------> [10, 20]
#        /
# b ----/
#
# Reference Count = 2
#
# Variables:
# a
# b


# ============================================================
# Example 3
# ============================================================

a = [10, 20]
b = a
c = a

# Memory:
#
# a ----\
#        \
# b ------> [10, 20]
#        /
# c ----/
#
# Reference Count = 3
#
# Variables:
# a
# b
# c


# ============================================================
# Example 4
# ============================================================

a = [10, 20]
b = a

del b

# Memory:
#
# a ---------> [10, 20]
#
# Reference Count = 1
#
# 'b' no longer exists.


# ============================================================
# Example 5
# ============================================================

a = [10, 20]
b = a

a = None

# Memory:
#
# a ---------> None
#
# b ---------> [10, 20]
#
# Reference Count = 1
#
# 'a' now points to None.
# Only 'b' points to the list.


# ============================================================
# Example 6
# ============================================================

a = [10, 20]
b = a

del a
del b

# Memory:
#
# No variable points to [10,20]
#
# Reference Count = 0
#
# Python Garbage Collector can free this object.


# ============================================================
# copy() Example
# ============================================================

a = [10, 20]
b = a.copy()

# Memory:
#
# a ---------> [10,20]
#
# b ---------> [10,20]
#
# These are TWO DIFFERENT list objects.
#
# Reference Count of first list = 1
# Reference Count of second list = 1
#
# copy() creates a NEW object.
# It does NOT increase the reference count.


# ============================================================
# Mutable Example
# ============================================================

a = [10, 20]
b = a

b.append(30)

print(a)
print(b)

# Output
# [10, 20, 30]
# [10, 20, 30]
#
# Why?
#
# Because both variables point to the SAME object.
#
# Reference Count = 2


# ============================================================
# Reassign Variable
# ============================================================

a = [10, 20]
b = a

a = [100]

print(b)

# Output
# [10, 20]
#
# Why?
#
# 'a' now points to a NEW list.
# 'b' still points to the OLD list.
#
# OLD list Reference Count = 1
# NEW list Reference Count = 1


# ============================================================
# Garbage Collection
# ============================================================

a = [1, 2, 3]

a = None

# The list now has no reference.
#
# Reference Count = 0
#
# Python's Garbage Collector will eventually
# remove this unused object from memory.


# ============================================================
# Important Notes
# ============================================================

# 1. Variables DO NOT store actual data.
#
# Variables store references (addresses) of objects.

# 2. Objects are created in Heap Memory.

# 3. Variables point to those objects.

# 4. Reference Count =
#    Number of variables pointing to the same object.

# 5. When Reference Count becomes 0,
#    the object becomes eligible for garbage collection.

# 6. copy() creates a new object.

# 7. Assignment (=) copies only the reference,
#    NOT the actual object.

# ============================================================
# Interview Questions
# ============================================================

# Q1
a = [10]
# Reference Count = ?


# Q2
a = [10]
b = a
# Reference Count = ?


# Q3
a = [10]
b = a
c = a
# Reference Count = ?


# Q4
a = [10]
b = a
del b
# Reference Count = ?


# Q5
a = [10]
b = a
a = None

print(b)

# Questions:
#
# 1. Output?
# 2. Reference Count?
# 3. Will the list be deleted?


# ============================================================
# GOLDEN RULE
# ============================================================

# Reference Count =
#
# Number of variables pointing to the SAME object.
#
# More references  -> Higher Reference Count
# Fewer references -> Lower Reference Count
# Zero references  -> Garbage Collector can free the object.