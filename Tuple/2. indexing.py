
fruits = ("Apple", "Banana", "Mango", "Orange")
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])

# negative indexing
# print(fruits[-1])
# print(fruits[-2])
# print(fruits[-3])
# print(fruits[-4])

# Dynamic indexing
numbers =  (10, 20, 30, 40, 50)
# index = int(input("Enter index: "))
# print(numbers[index])

# nested tuple indexing
data = (
    (10, 20),
    (30, 40),
    (50, 60)
)
print(data[0])
print(data[0][1])

# deep nested tuple
t = (
    10,
    (
        20,
        (
            30,
            40
        )
    )
)
print(t[1][1][1])