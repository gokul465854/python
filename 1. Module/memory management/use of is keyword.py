a = [10,20]
b = [10,20]
print(type(a))
print(type(b))
print(a is b) # False because list is mutable
print(a == b) # true because == operator compare to value

a = {"Name": "Jai"}
b = {"Name": "Jai"}
print(type(a))
print(type(b))
print(a is b) # False because Dictionary is mutable
print(a == b) # true because == operator compare to value

a = {"Name", "Jai"}
b = {"Name", "Jai"}
print(type(a))
print(type(b))
print(a is b) # False because set is mutable
print(a == b) # true because == operator compare to value



