#Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.
sum = 0
while sum<=100 :
    n = int(input("Enter a number : "))
    sum = sum+n
print("Sum = ",sum)