'''
Recursion ke 2 Parts
Har recursive function me 2 cheezein zaroor honi chahiye.
1️.Base Case --> Jahan recursion rukta hai.
2️.Recursive Case --> Jahan function dobara khud ko call karta hai.
'''
def countdown(n):
    if n == 0: # base case
        return
    print(n)
    countdown(n - 1) # recursive case
countdown(5)