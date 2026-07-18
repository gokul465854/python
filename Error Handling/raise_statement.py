
# def check_age(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero and negative.")
#     return age

# try:
#     num = int(input("Enter age: "))
#     result = check_age(num)
# except ValueError as e:
#     print(f'Error: {e}')
# else:
#     print(f'Age: {result}')
# finally:
#     print("Execution completed.")


# The raise statement can also be used to re-raise the current exception, which is particularly useful in exception handling:

def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print("Logging: Invalid data received")
        raise 
    
try:
    process_data('abc')
except ValueError:
    print("Handle at higher level")

# You can create and raise custom exceptions by defining your own exception classes: 

# class InsufficientFundsError(Exception):
#     def __init__(selt, balance, amount):
        