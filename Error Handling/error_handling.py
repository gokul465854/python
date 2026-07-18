
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid integer.")


# Use Exception to catch almost all errors.
try:
    x = int(input("Enter number: "))
    print(100 / 0)
except Exception as e:
    print('Error:', e)

# The else block executes only if no exception occurs.
try:
   num = int(input("Enter numbers: "))
   result = 10 / num
except ZeroDivisionError:
   print("Cannot divide by zero")
else:
   print("Result =", result)


# The finally block always executes whether an exception occurs or not.

try:
   num = int(input("Enter number: "))
   result = 10 / num
except ZeroDivisionError:
   print("Cannot divide by zero.")
finally:
   print("Program ended.")

# completer example

try:
   num = int(input("Enter Number: "))
   result = 10 / num
except ValueError:
   print("Please enter valide input")
except ZeroDivisionError:
   print("Cannot divide by zero")
else:
   print("Result: ", result)
finally:
   print("Execution completed.")

# Raising Exceptions Manually - You can generate your own exception using raise.
age = int(input("Enter age: "))

if age < 0:
   raise ValueError("Age cannot be negative")

print("Age:", age)