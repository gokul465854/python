# ========================== sort() and sorted() methods======================================
# sorting ascending order
a = [4,3,5,2,6,9]
a.sort()
print(a)

# sorting descending order
b = [7,3,2,6,8,4,9]
b.sort(reverse = True)
print(b)

# sort string alphabetically
words = ["banana","mango","apple"]
words.sort()
print(words)

# use sorted() on string
print(sorted("jai"))

# sort by length using key=len
words.sort(key=len)
print(words)

# sort list without changing original list
num = [4,6,2,8,5,9,3]
print("original list: ", num)
sorted_list = sorted(num)
print("sorted list: ", sorted_list)

# ==================================== reverse() and reversed() methods============
# check if list is palindrome using reverse
num_list = [3,2,3]
reversed_list = list(reversed(num_list))
if num_list == reversed_list:
    print("it is palindrome")
else:
    print("not palindrome")

# Reverse user input.
# user = input("enter number or words: ")
# user_reversed_list = list(reversed(user))
# print(user_reversed_list)

# Reverse without using reverse()
l = [1,2,3,4,5]
print(l[::-1])

# ========================== shallow copy(),list() and slicing ===============================
a = [[10,20],[30,40]]

b = list(a)

c = a[:]

b.append([50])

c[1].append(99)

print(a)

print(b)

print(c)

print(a[1] is c[1])

print(id(a))

print(id(b))

print(id(c))

# =================== deepcopy() =======================
import copy
a = [
    [1,2],
    [3,[5,6]]
]
b = copy.deepcopy(a)
b[1][1].append(99)
print(b)