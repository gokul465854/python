marks = int(input("Enter your marks(0-100): "))

if marks in range(0,40):
    print("Grade: F")
elif marks in range(41,50):
    print("Grade: C")
elif marks in range(51,60):
    print("Grade: B")
elif marks in range(61,70):
    print("Grade: B+")
elif marks in range(71,80):
    print("Grade: A")
elif marks in range(81,90):
    print("Grade: A+")
elif marks in range(91,101):
    print("Grade: A++")
else:
    print("invalid marks")
