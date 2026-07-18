temperature = float(input("Enter a temperature in Celsius: "))

if temperature in range(0,10):
    print("The weather is cold")
elif temperature in range(10,30):
    print("The weather is warm")
else:
    print("The weather is hot")

