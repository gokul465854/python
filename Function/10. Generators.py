'''
Generators: Normal function return karta hai aur khatam ho jata hai.
Generator function yield use karta hai, jisse function pause ho jata
hai aur baad me wahi se resume kar sakta hai.
'''
def simple_gen():
    print("First Value")
    yield 1
    print("Second value")
    yield 2
    print("Third value")
    yield 3

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))