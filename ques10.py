
#Write a program to find whether the entered number is a multiple of both 3 and 7.
num = int(input("Enter the number : "))
if num%3==0 and num%7==0 :
    print(num,"is a multiple of both 3 and 7")
else :
    print(num,"is not a multiple of both 3 and 7")