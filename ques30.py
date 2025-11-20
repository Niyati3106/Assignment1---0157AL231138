#Write a program that accepts a number from the user and prints whether it is a Strong number (sum of factorials of digits = number itself) using a for loop. Example: 145 => 1! + 4! + 5! = 145.
from math import factorial
n = int(input("Enter a number : "))
str_n = str(n)
sum= 0 
for i in str_n :
    sum = sum + factorial(int(i))
if sum == n :
    print(n, " is a strong number")
else :
    print(n, " is not a strong number")