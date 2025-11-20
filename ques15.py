#Write a program to check if a character is uppercase, lowercase, digit, or special symbol.
ch = input("Enter a character : ")
if ch>='A' and ch<='Z' :
    print("Uppercase character")
elif ch>='a' and ch<='z':
    print("Lowercase character")
elif ch>='0' and ch<='9' :
    print("Character is a digit")
else :
    print("Character is a special character")