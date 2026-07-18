"""
1. issubset() --> if all element of set A are present in the set B,
then A is subset of B (A ⊆ B)"""
# Example 1
A = {1,2,3}
B = {1,2,3,4,5}
print(A.issubset(B))

# Example 2
A = {1, 5}
B = {1, 2, 3, 4}
print(A.issubset(B))

"""
2. issuperset() --> all element set B are present in the set A, 
then set A is superset of B
"""
A = {1,2,3,4,5}
B = {1,2,3}
print(A.issuperset(B))

"""
3. isdisjoint() --> no common element present in the both sets 
the A is disjoint of B"""
A = {1,2,3}
B = {4,5,6}
print(A.isdisjoint(B))

# Operators
# subset
A = {1,2}
B = {1,2,3}
print(A <= B)
# Equivalent to the --> A.issubset(B)
# proper subset
print(A < B)

# superset
A = {1,2,3}
B = {2,3}
print(A >= B) # Equivalent to the --> A.issuperset(B)

# Permission Check
required = {
    "read",
    "write"
}
user = {
    "read",
    "write",
    "delete"
}
print(required.issubset(user))

# Course Completion
required = {
    "Python",
    "SQL"
}
completed = {
    "Python",
    "SQL",
    "Java"
}
print(required <= completed)

# Duplicate User Check
group1 = {
    "Ram",
    "Shyam"
}
group2 = {
    "Mohan",
    "Raju"
}
print(group1.isdisjoint(group2))

# Without running the code, predict the output
A = {1, 2}
B = {1, 2, 3}
C = {4, 5}

print(A <= B)
print(A < B)
print(B >= A)
print(B > A)
print(A.isdisjoint(C))
print(B.isdisjoint({2, 6}))
print(A <= A)
print(A < A)