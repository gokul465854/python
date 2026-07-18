# List Comprehensions

# A list comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.

# Default method to create a list of even numbers from 1 to 20
even_numbers = []

for num in range(1,21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Using list comprehension to create a list of even numbers from 1 to 20
# even_numbers = [num for num in range(1,21) if num % 2 == 0]
# print (even_numbers)

# another example of list comprehension to create a list of odd and even numbers from 1 to 5
numbers = [1,2,3,4,5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)  # Output: [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]

# filter() fuction - The filter() function is a built-in function in Python that allows you to filter elements from an iterable (like a list) based on a specified condition. It takes two arguments: a function that defines the filtering condition and an iterable to be filtered. The filter() function returns an iterator that contains only the elements from the original iterable that satisfy the condition defined by the function. 

words = ['tree', 'sky', 'mountain', 'river', 'sun','cloud']

def is_long_word(word):
  return len(word) > 4 

long_words = list(filter(is_long_word, words))
print(long_words)  # Output: ['mountain', 'river', 'cloud']

# map() function - The map() function is a built-in function in Python that allows you to apply a specified function to each item of an iterable (like a list) and return an iterator that yields the results. It takes two arguments: a function that defines the operation to be applied and an iterable to which the function will be applied. The map() function returns an iterator that produces the results of applying the function to each item in the iterable.

celsius = [0, 10, 20, 30, 40] 

def to_fahrenheit(temp):
  return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]

# sum() function - The sum() function is a built-in function in Python that calculates the sum of all the elements in an iterable (like a list, tuple, or set) and returns the total. It takes an iterable as its argument and adds up all the numeric values contained within it. The sum() function can also take an optional second argument, which is the starting value for the summation. If provided, this value is added to the total sum of the elements in the iterable.

numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
print(total_sum)  # Output: 15

# positinal argument - A positional argument is a type of argument that is passed to a function based on its position or order in the function's parameter list. 

number = [5,10,15,20]
total = sum(number, 10)  # Here, 10 is a positional argument that serves as the starting value for the summation.
print(total)  # Output: 60 (10 + 5 + 10 + 15 + 20 = 60)

