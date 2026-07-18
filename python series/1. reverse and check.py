# write a program that will reverse a four digits number and Also check is reversed is true

num = input('Enter a number: ')

if len(num) == 4 and num.isdigit():
    reverse = num[::-1]
    print(reverse)
else:
    print("Please enter a valid number")
if reverse == num[::-1]:
    print("Yes, it is reverse the number")
