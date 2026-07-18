# reverse list without using reverse()
from functools import lru_cache
from operator import mul

l = [1,2,3,4,5]
left = 0
right = len(l) -1
while left < right:
    l[left],l[right] = l[right],l[left]
    left +=1
    right -= 1
# print(l)

# pair sum target = 9
num = [1,2,3,4,5,6]
lef = 0
right = len(num) - 1
target = 9
while left < right:
    if num[left] + num[right] == target:
        # print(num[left],num[right])
        break
    elif num[left] + num[right] < target:
        left +=1
    else:
        right -= 1

# reverse a string
name = 'Sakshi'
left = len(name)
right = len(name) -1

while left < right:

    left +=1
    right -= 1
print(name)

# concatenation list
list = [1,2,3]
n = len(list)
ans = [0] * (2 * n)
for i in range(n):
    ans[i] = list[i]
    ans[i + n] = list[i]
print(ans)