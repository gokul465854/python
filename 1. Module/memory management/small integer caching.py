# ============================================================
# PYTHON SMALL INTEGER CACHING - COMPLETE NOTES
# ============================================================

# ------------------------------------------------------------
# What is Small Integer Caching?
# ------------------------------------------------------------
#
# Small Integer Caching is an optimization used by CPython.
#
# CPython creates integer objects from -5 to 256 only once.
#
# Whenever these values are needed,
# Python reuses the existing objects.
#
# Simple Definition:
#
# "CPython caches integers from -5 to 256
# and reuses them instead of creating new objects."
#
# ------------------------------------------------------------


# ============================================================
# Why is Small Integer Caching Needed?
# ============================================================

# Imagine millions of programs use numbers like:
#
# 0
# 1
# 2
# 10
# 100
# 255
#
# Creating a new object every time would waste memory.
#
# So Python keeps these integer objects ready
# and reuses them.


# ============================================================
# Cached Integer Range
# ============================================================

# CPython caches:
#
# -5  to  256
#
# This range is implementation-specific.
#
# It is NOT guaranteed by the Python language.


# ============================================================
# Example 1
# ============================================================

a = 10
b = 10

print(a is b)

# Output (CPython)
#
# True
#
# Reason:
#
# 10 is inside the cached range.


# ============================================================
# Example 2
# ============================================================

a = 256
b = 256

print(a is b)

# Usually
#
# True
#
# Because 256 is cached.


# ============================================================
# Example 3
# ============================================================

a = -5
b = -5

print(a is b)

# Usually
#
# True
#
# Because -5 is cached.


# ============================================================
# Example 4
# ============================================================

a = 257
b = 257

print(a is b)

# Result may vary.
#
# Sometimes True.
# Sometimes False.
#
# It depends on:
#
# - Python implementation
# - Execution context
# - Compiler optimizations


# ============================================================
# Memory Representation
# ============================================================

# Cached Integer
#
#            10
#             ▲
#       ┌─────┴─────┐
#       │           │
#       a           b
#
# Both variables point to the SAME object.


# ============================================================
# Why Only Small Integers?
# ============================================================

# Small integers are used extremely frequently.
#
# Examples:
#
# Loop counters
#
# for i in range(10):
#
#
# Boolean calculations
#
# Indexing
#
# Counting
#
# Length calculations
#
# Memory addresses
#
# Therefore,
# caching them improves performance.


# ============================================================
# Does Python Cache Every Integer?
# ============================================================

# No.
#
# Caching every integer would waste memory.
#
# Imagine caching:
#
# 999999999999
#
# 87546329874
#
# These numbers may never be used again.


# ============================================================
# Difference Between Object Interning
# and Small Integer Caching
# ============================================================

#
# Object Interning
#
# General optimization.
#
# Mostly for immutable objects
# like strings.
#
#
# Small Integer Caching
#
# Specific optimization
# only for integers
# (-5 to 256 in CPython).


# ============================================================
# Important Notes
# ============================================================

# 1.
# Small Integer Caching is a CPython optimization.
#
# 2.
# Python language does NOT guarantee this behavior.
#
# 3.
# Never write code that depends on it.
#
# 4.
# Always compare integer values using ==
#
# NOT using "is"


# ============================================================
# Correct Comparison
# ============================================================

a = 1000
b = 1000

print(a == b)

# Correct
#
# True


print(a is b)

# Never rely on this result.
#
# It depends on implementation.


# ============================================================
# Interview Questions
# ============================================================

# Q1
#
# What is Small Integer Caching?

# Q2
#
# Which integer range is cached in CPython?

# Q3
#
# Why does Python cache small integers?

# Q4
#
# Is Small Integer Caching guaranteed
# by the Python language?

# Answer:
#
# No.

# Q5
#
# Difference between
#
# Object Interning
#
# and
#
# Small Integer Caching?


# ============================================================
# GOLDEN FLOW
# ============================================================

# Integer Created
#        │
#        ▼
# Is Integer between -5 and 256 ?
#        │
#   ┌────┴────┐
#   │         │
#  Yes        No
#   │         │
#   ▼         ▼
# Reuse     Create New
# Cached    Integer Object
# Object


# ============================================================
# GOLDEN RULE
# ============================================================

# CPython caches integers
#
# -5 to 256
#
# to save memory
# and improve performance.
#
# Never use "is"
# for comparing numbers.
#
# Always use
#
# ==
#
# for value comparison.
# ============================================================