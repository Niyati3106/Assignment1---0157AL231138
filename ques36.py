#Write a program to repeatedly accept a string from the user until the string entered is a palindrome.
is_palindrome = False
while is_palindrome == False :
    s = input("Enter a string : ")
    if s == s[::-1]:
        is_palindrome = True
print(s, " : is a palindrome string")