# from os import access
#
# fruits = ["apple:6", "banana: 4", "Mango: 3",45,3.4,True,False]
# # print(fruits)
#
# # empty list
# my_list = []
# # print(my_list)
#
# # integer list
# numbers = [1,2,3,4,5,6,7,8,9]
# # print(numbers[0]) #access first element
# # print(numbers[4])
# # print(numbers)
#
# # String list
# colors = ["red", "yellow", "pink"]
# # print(colors)
#
# # mixed list
# mixed = ["apple: 6", "banana: 4", "Mango: 3",45,3.4,True,False]
# # print(mixed)
#
# # Nested list
# matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# # print(matrix)
#
# # print(matrix[-1])
#
# nums = ['banana', 'apple', 'mango', 34,43.3,True]
# # print(nums[3:6])
#
# # print(nums[::-1])
# # print(nums[::2])
# # print(nums[1:5:2])
#
# # update list
# list = ["mango","apple","banana","cherry",23,"jai",True]
# index = 0
# for item in list:
#     print(f"{index}: {item}")
#     index += 1
#
# # list[4] = "Sita Fal"
# # list[6] = "Kundan"
#
# print(list)
#
# list[4:7:2] = ["Gokul", "Python"]
# print(list)
#
# list.append("mango")
# print(list)
#
# list.extend(["banana","apple","Tamatar"])
# print(list)
#
# list.insert(0,"appple")
# print(list)
#
# list.remove("mango")
# print(list)
#
# list.pop(7)
# print(list)
#
# # list.clear()
# # print(list)
#
# # del list[1]
# # print(list)
#
# # del list[2:7]
# # print(list)
#
# # print(len(list))
# # print(max(list))
# # print(min(list))
# # print(sum(numbers))
# #
# # print(sorted(numbers))
# #
# # print(34 not in numbers)
# # print("Chandan" in list)
# #
# # print(list.copy())
# #
# # print(list.index("jai"))

# List comprehension

squares = [x**2 for x in range(11)]
print(squares)

# with if conditions
squ = [x**2 for x in range(11) if x % 2 == 0]
print(squ)

# nested comprehension
matrix = [[i*j for j in range(3)]for i in range(3)]
print(matrix)