#Write a program to display the smallest number number among three numbers using nested if.
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

if num1<=num2 :
    if num1<=num3 :
        print(num1," is the smallest")
    else :
        print(num3," is the smallest")
else :
    if num2<=num3 :
        print(num2," is the smallest")
    else :
        print(num3," is the smallest")