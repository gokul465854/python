# ============================================================
# PYTHON OBJECT INTERNING - COMPLETE NOTES
# ============================================================

# ------------------------------------------------------------
# What is Object Interning?
# ------------------------------------------------------------
#
# Object Interning is an optimization technique used by Python.
#
# Instead of creating multiple identical immutable objects,
# Python may reuse an existing object.
#
# Simple Definition:
#
# "Python reuses existing immutable objects
# instead of creating new ones."
#
# This saves memory and improves performance.
#
# ------------------------------------------------------------


# ============================================================
# Why is Object Interning Needed?
# ============================================================

# Suppose your program contains:

a = 10
b = 10
c = 10
d = 10

# Without Interning:
#
# a ----> 10
# b ----> 10
# c ----> 10
# d ----> 10
#
# Four separate objects would waste memory.


# With Interning:
#
#            10
#             ▲
#      ┌──────┼──────┐
#      │      │      │
#      a      b      c
#                    │
#                    d
#
# Only ONE object is created.
#
# All variables point to the same object.


# ============================================================
# Example 1 - Integer
# ============================================================

a = 10
b = 10

print(a is b)

# Output (Usually in CPython)
#
# True
#
# Reason:
#
# Python reused the same integer object.


# ============================================================
# Example 2 - String
# ============================================================

a = "Python"
b = "Python"

print(a is b)

# Output (Usually)
#
# True
#
# Reason:
#
# Python often interns identical strings.


# ============================================================
# Example 3 - List
# ============================================================

a = [10, 20]
b = [10, 20]

print(a is b)

# Output
#
# False
#
# Reason:
#
# Lists are mutable.
#
# Python creates two different objects.


# ============================================================
# Why Doesn't Python Intern Lists?
# ============================================================

a = [10, 20]
b = [10, 20]

# Suppose Python reused the same object.
#
#          [10,20]
#             ▲
#        ┌────┴────┐
#        │         │
#        a         b

a.append(30)

# If both variables pointed to the same list,
#
# b would also become
#
# [10,20,30]
#
# This would cause unexpected side effects.
#
# Therefore,
# Python creates separate mutable objects.


# ============================================================
# Commonly Interned Objects
# ============================================================

# Usually (CPython):
#
# Small Integers
#
# Example:
#
# 10
# 100
# 256
#
# Strings
#
# Example:
#
# "Python"
# "Hello"
#
# Some Tuples
#
# (when they contain immutable objects)


# ============================================================
# Objects That Are NOT Interned
# ============================================================

# List
#
# []

# Dictionary
#
# {}

# Set
#
# set()

#
# These are mutable objects.
#
# Python creates a new object every time.


# ============================================================
# == vs is
# ============================================================

a = "Python"
b = "Python"

print(a == b)
print(a is b)

# Output
#
# True
# True
#
# ==
#
# Compares values.
#
# is
#
# Compares object identity.


# ------------------------------------------------------------

a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)

# Output
#
# True
# False
#
# Values are equal.
#
# Objects are different.


# ============================================================
# Important Note
# ============================================================

a = 1000
b = 1000

print(a is b)

# Result may vary.
#
# Sometimes True.
# Sometimes False.
#
# Depending on Python implementation,
# optimization,
# and execution context.
#
# Therefore,
#
# NEVER compare values using "is".
#
# Always use
#
# ==


# ============================================================
# Real-Life Example
# ============================================================

# Imagine a library.
#
# 100 students want the same book.
#
# The library does NOT print 100 copies.
#
# Instead,
# everyone uses the same book.
#
# Python does the same thing
# with immutable objects.


# ============================================================
# Advantages of Object Interning
# ============================================================

# 1. Saves Memory.
#
# 2. Improves Performance.
#
# 3. Avoids creating duplicate immutable objects.
#
# 4. Faster identity comparison.


# ============================================================
# Disadvantages
# ============================================================

# Object Interning is an optimization.
#
# You should NEVER rely on it
# for program logic.


# ============================================================
# Important Notes
# ============================================================

# 1. Object Interning mainly works with
#    immutable objects.
#
# 2. Mutable objects are NOT automatically interned.
#
# 3. "==" compares values.
#
# 4. "is" compares object identity.
#
# 5. Never use "is" for value comparison.


# ============================================================
# Interview Questions
# ============================================================

# Q1
#
# What is Object Interning?

# Q2
#
# Why does Python use Object Interning?

# Q3
#
# Why are Lists not interned?

# Q4
#
# Difference between
#
# ==
#
# and
#
# is

# Q5
#
# Why is Object Interning useful?

# Q6
#
# Can you rely on Object Interning
# for program logic?
#
# Answer:
#
# No.


# ============================================================
# GOLDEN FLOW
# ============================================================

# Immutable Object Created
#          │
#          ▼
# Does an identical interned object exist?
#          │
#      ┌───┴───┐
#      │       │
#     Yes      No
#      │        │
#      ▼        ▼
# Reuse Object  Create New Object
#
# Memory Saved
# Performance Improved


# ============================================================
# GOLDEN RULE
# ============================================================

# Immutable Objects
#
# Python MAY reuse the same object.
#
# (Object Interning)
#
# Mutable Objects
#
# Python creates a NEW object every time.
#
# Never use "is" to compare values.
#
# Use "==" for value comparison.
#
# Use "is" only to check whether two variables
# refer to the SAME object.
#
# Example:
#
# if obj is None:
#     ...
# ============================================================