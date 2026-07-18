# ============================================================
# PYTHON GARBAGE COLLECTOR (GC) - COMPLETE NOTES
# ============================================================

# ------------------------------------------------------------
# What is Garbage Collector (GC)?
# ------------------------------------------------------------
# Garbage Collector (GC) is Python's automatic memory
# management system.
#
# It automatically frees the memory of objects that are
# no longer being used.
#
# Simple Definition:
#
# "Garbage Collector removes unused objects from memory."
#
# ------------------------------------------------------------


# ============================================================
# Why do we need Garbage Collector?
# ============================================================

# Example

a = [10, 20]

# Memory
#
# a ---------> [10,20]
#

a = None

# Memory
#
# a ---------> None
#
# [10,20]
#
# The list is no longer used.
#
# If Python never removed this list,
# memory would keep filling up.
#
# Garbage Collector helps free this unused memory.


# ============================================================
# Relationship Between Reference Count and GC
# ============================================================

# Reference Count tells:
#
# "How many variables point to an object?"
#
# Garbage Collector:
#
# Cleans unused objects from memory.
#
# IMPORTANT
#
# In CPython:
#
# If Reference Count becomes 0,
# the object is usually destroyed immediately
# by the reference counting mechanism.
#
# Garbage Collector mainly handles
# Circular References.


# ============================================================
# Example 1
# ============================================================

a = [1, 2, 3]

# Reference Count = 1

a = None

# Reference Count = 0
#
# The list is no longer referenced.
#
# In CPython, it becomes eligible for immediate destruction.


# ============================================================
# Example 2
# ============================================================

a = [1]
b = a

# Reference Count = 2

del a

# Reference Count = 1

print(b)

# Output
#
# [1]
#
# Object is NOT deleted because
# variable 'b' still points to it.


# ============================================================
# Example 3
# ============================================================

a = [1]
b = a

del a
del b

# Reference Count = 0
#
# No variable points to the object.
#
# Memory can now be released.


# ============================================================
# Circular Reference Problem
# ============================================================

a = []
b = []

a.append(b)
b.append(a)

# Memory
#
# a --------\
#            \
#             ---> []
#                 |
#                 |
#                 ▼
#             <--- []
#            /
# b --------/
#
# a points to b
#
# b points to a


del a
del b

# Even after deleting variables,
# both objects still reference each other.
#
# Reference Counting alone cannot clean them.
#
# Garbage Collector detects this circular
# reference and removes it.


# ============================================================
# Manually Running Garbage Collector
# ============================================================

import gc

gc.collect()

# gc.collect()
#
# Requests Python to run the Garbage Collector.
#
# Normally you DO NOT need to call this yourself.


# ============================================================
# Advantages of Garbage Collector
# ============================================================

# 1. Automatically frees unused memory.
#
# 2. Prevents many memory leaks.
#
# 3. No need to manually free memory
#    like in C language.
#
# 4. Makes programming easier.


# ============================================================
# Disadvantages
# ============================================================

# 1. Garbage Collection can occasionally
#    pause program execution briefly.
#
# 2. Exact cleanup timing is not always predictable.


# ============================================================
# Reference Counting vs Garbage Collector
# ============================================================

# Reference Counting
#
# - Counts references.
# - Detects when reference count becomes 0.
# - In CPython, objects with count 0 are usually
#   destroyed immediately.


# Garbage Collector
#
# - Finds unreachable objects.
# - Cleans circular references.
# - Frees memory occupied by unreachable objects.


# ============================================================
# Important Notes
# ============================================================

# 1. Python automatically manages memory.
#
# 2. Objects are created in Heap Memory.
#
# 3. Variables store references, not actual data.
#
# 4. If no variable points to an object,
#    its Reference Count becomes 0.
#
# 5. In CPython, such objects are usually
#    destroyed immediately.
#
# 6. Garbage Collector mainly removes
#    Circular References.


# ============================================================
# Interview Questions
# ============================================================

# Q1
#
# What is Garbage Collector?

# Q2
#
# Why do we need Garbage Collector?

# Q3
#
# What happens when Reference Count becomes 0?

# Q4
#
# Difference between
# Reference Counting
# and
# Garbage Collector?

# Q5
#
# What is Circular Reference?

# Q6
#
# Why can't Reference Counting alone
# solve Circular References?


# ============================================================
# GOLDEN FLOW
# ============================================================

# Object Created
#        │
#        ▼
# Reference Count = 1
#        │
#        ▼
# More Variables
#        │
#        ▼
# Reference Count Increases
#        │
#        ▼
# Variables Deleted
#        │
#        ▼
# Reference Count Decreases
#        │
#        ▼
# Reference Count = 0
#        │
#        ▼
# (CPython)
# Object is usually destroyed immediately
#        │
#        ▼
# Garbage Collector additionally handles
# Circular References.


# ============================================================
# GOLDEN RULE
# ============================================================

# Variables hold REFERENCES.
#
# Objects live in HEAP MEMORY.
#
# Reference Count tracks how many references
# point to an object.
#
# When no references remain,
# the object becomes unreachable.
#
# In CPython, it is usually destroyed immediately.
#
# Garbage Collector mainly cleans
# Circular References.