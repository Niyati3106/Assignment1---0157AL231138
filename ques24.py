''' Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4:

*
***
*****
*******'''

n = int(input("Enter the number : "))
for i in range(1, n + 1):
        
        for j in range(n - i):
            print(" ", end=" ")
        
        for k in range(1, 2*i):
            print("*", end=" ")
        print()