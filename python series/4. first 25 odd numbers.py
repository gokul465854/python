# count_odd = 0
#
# for i in range(1,51):
#     if i % 2!= 0:
#         print(i)
#         count_odd = count_odd + 1
#     if count_odd == 25:
#         break
#
# #  short trick
#
# for i in range(1,51,2):
#     print(i)
#
# using while loop
count = 0
i = 1
while count < 25:
    if i % 2 != 0:
        print(i)
        count = count + 1

    i = i + 1