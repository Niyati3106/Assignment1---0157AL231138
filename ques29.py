#Write a program using a for loop to display the sum of the series:
#12 + 22 + 32 + ... + n2
n = int(input("Enter a number : "))
sum=0
for i in range (1,n+1) :
    sum = sum + (i**2)
print("Sum = ",sum)