
#Write a program to determine the largest of four numbers using nested if.
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
num4 = int(input("Enter fourth number : "))

if(num1>=num2) :
    if(num1>=num3) :
        if(num1>=num4) :
            print(num1," is the greatest")
        else :
            print(num4," is the greatest")
    else :
        if(num3>=num4) :
            print(num3," is the greatest")
        else :
            print(num4," is the greatest")
else :
    if num2>=num3 :
        if num2>=num4 :
            print(num2," is the greatest")
        else :
            print(num4," is the greatest")
    else :
        if num3>=num4 :
            print(num3," is the greatest")
        else :
            print(num4," is the greatest")