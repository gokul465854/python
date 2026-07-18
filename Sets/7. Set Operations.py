# 1. Union ( ∪ ) --> |
# unique element of two sets
A = {1,2,3}
B = {3,4,5}
print(A | B)
# or
print(A.union(B))

# 2. Intersection ( ∩ ) --> &
# common element of two sets
A = {1,2,3}
B = {3,4,5}
print(A & B)
# or
print(A.intersection(B))

# 3. Difference ( - )
# A me jo hai lekin B me nahi.
A = {1,2,3}
B = {3,4,5}
print(A - B)
print(A.difference(B))

# reverse
print(B - A)
print(B.difference(A))

# 4. Symmetric Difference ( ^ )
# jo common nahi hai
# formula: (A - B) + (B - A)
A = {1,2,3}
B = {3,4,5}
print(A ^ B)
print(A.symmetric_difference(B))

# multiple sets
# 1 .Union
A = {1}
B = {2}
C = {3}
print(A | B | C)
print(A.union(B,C))

# 2. intersection
A = {1,2,3}
B = {2,3}
C = {3}
print(A & B & C)
print(A.intersection(B,C))

# Time Complexity
# len(A)=n
# len(B)=m

# Operation	                Complexity
# Union           -->      	O(n + m)
# Intersection	  -->       O(min(n, m)) average
# Difference	  -->       O(n) average
# Symmetric Difference	--> O(n + m)

# Find common students enrolled in two courses
course1 = {"jai","sakshi","kundan","gokul"}
course2 = {"sakshi","kundan","chandan","kittu"}
common = course1.intersection(course2)
print(course1 & course2)
print(common)

# Find subjects that only one student has taken.
student1 = {"math","physics","python"}
student2 = {"physics","java","math"}
diff = student1.symmetric_difference(student2)
print(diff)
print(student1 ^ student2)

# Find all unique visitors from two days
day1 = {"A","B","C","D"}
day2 = {"C","D","E","F"}
all_visitors = day1.union(day2)
print(all_visitors)
print(day1 | day2)

# Check whether two sets have any common elements using intersection
set1 = {1,2,3}
set2 = {3,4,5}

if set1.intersection(set2): #if set1 & set2:
    print("common element exited")
else:
    print("no common exited")

# Perform the same operations using both operators and methods
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# union - method
print(A.union(B))
# union - operator
print(A | B)

# intersection - method
print(A.intersection(B))
# intersection - operator
print(A & B)

# Difference - method (A -B)
print(A.difference(B))
# difference - operator
print(A - B)

# Difference - method (B - A)
print(B.difference(A))
# Difference - operator
print(B - A)

# symmetric difference - method
print(A.symmetric_difference(B))
# symmetric difference - operator
print(A ^ B)

# Predict the output without running the code:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)
print(A & B)
print(A - B)
print(B - A)
print(A ^ B)
print((A | B) - (A & B))