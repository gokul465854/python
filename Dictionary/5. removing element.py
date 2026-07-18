# del --> remove by key
from linecache import clearcache

d = {
    "a": 1,
    "b": 2,
    "c": 3
}
del d["b"]
# print(d)

# pop() --> remove by key + return value
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
val = d.pop("b")
# print(val)
# print(d)

# popitem() --> remove last inserted element
dataList = {
    "name": "jai",
    "age": 21,
    "subjest": "math",
    "marks": 89
}
# item = dataList.popitem()
# print(item)
# print(dataList)

# clear() --> remove all element
infoList = dataList
# infoList.clear()
# print(infoList)

# safe deletion
# method - 1
d = {
    "A": 1,
    "B": 2,
    "C": 3
}
popItem = "B"
if popItem in d:
    d.pop(popItem)
    # print(d)
else:
    print("key does't not exited")

