#Write a program to generate Pascal’s Triangle up to n rows using a for loop.
from math import factorial
n = int(input("Enter a number : "))
for i in range(n):
    for j in range(n-i+1) :
        print(end=" ")

    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()