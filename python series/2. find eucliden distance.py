import math

# write a program to find euclidean distance between two cooradinate

x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())

distance = round(math.sqrt((x2-x1)**2 + (y2 - y1)**2),2)

print(distance)



