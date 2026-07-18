ch = input("Enter a character: ")

if len(ch) == 1 and ch.isalpha():
    ch = ch.lower()

    if ch in ["a", "e", "i", "o", "u"]:
        print("It is a vowel")
    else:
        print("It is a consonant")
else:
    print("Invalid input")