#Write a program to find the greatest of two numbers.
num1 = int (input("Enter first number : "))
num2 = int (input("Enter second number : "))
if(num1>num2) :
    print("Greatest number : ",num1)
elif(num2>num1) :
    print("Greatest number : ",num2)
else :
    print("Both numbers are equal")