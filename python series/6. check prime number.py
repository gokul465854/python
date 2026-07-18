
num = int(input("Enter number to check, its prime or not: "))

i = 2
if(num < i):
    print("It is not prime number")
elif num > i:
    while num > i:
        if num % i == 0:
            print("It is not prime number")
            break
    i = i + 1
else:
    print("It is prime number")

