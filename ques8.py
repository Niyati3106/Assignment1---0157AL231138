#Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number.
num = int(input("Enter a num : "))
if num<10 and num>-10 :
    print("Single digit number")
elif num<100 and num>-100 :
    print("Two digit number")
else :
    print("More than two digits")