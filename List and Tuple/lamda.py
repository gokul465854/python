# Lambda Functions - A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.

def square(num):
  return num ** 2

print(square(5))  # Output: 25

numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

