ch = input("Enter character: ")

if len(ch) == 1:
    if ch.islower():
        print("It is lowercase character")
    elif ch.isupper():
        print("It is uppercase character")
    elif ch.isdigit():
        print("it is an integer")
    else:
        print("it is special character")
else:
    print("invalid input")