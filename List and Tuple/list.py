# List is a collection which is ordered and changeable. Allows duplicate members. 

# append() method - The append() method is a built-in function in Python that is used to add a single element to the end of a list. It takes one argument, which is the element you want to add, and modifies the original list in place. The append() method does not return any value; it simply updates the list by adding the new element at the end.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

even_numbers = [6,8,10]

numbers.append(even_numbers)
print(numbers)

# extend() method - The extend() method is a built-in function in Python that is used to add all the elements of an iterable (like a list, tuple, or set) to the end of a list. It takes one argument, which is the iterable you want to add, and modifies the original list in place. The extend() method does not return any value; it simply updates the list by adding each element from the iterable to the end of the list.
numbers.extend(even_numbers)
print(numbers)

numbers.insert(7,9)
print(numbers)

numbers.insert(6,7)
print(numbers)

numbers.remove(7)
print(numbers)

numbers.pop(2)
print(numbers)

even_numbers.clear()
print(even_numbers)

num = [6,5,4,3,2,1]
num.reverse()
print(num)


programing_languages = ['python','Java', 'C++']
print(programing_languages.index('Javas'))


developer = ('Alice', 34, 'Python Developer')
print(developer[-2])

