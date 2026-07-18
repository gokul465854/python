num = input("Enter a number, you want to check Armstrong number or not: ")

n = len(num)
result = 0

for digit_char in num:
    digit = int(digit_char)
    result = result + digit**n

if result == int(num):
    print("It is Armstrong number")
else:
    print("It not ")