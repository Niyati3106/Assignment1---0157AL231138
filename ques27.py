#Write a program that accepts a number from the user and prints whether it is a Harshad number (number divisible by the sum of its digits) using a for loop.
num = int(input("Enter a number : "))
sum = 0
str_num=str(num)
for i in str_num :
    sum = sum + int(i)
if num%sum==0 :
    print(num," is a Harshad number")
else :
    print(num," is not a Harshad number")