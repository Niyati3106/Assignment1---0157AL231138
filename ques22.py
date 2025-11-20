#Write a program to generate and display the first n prime numbers using a for loop.
n = int(input("Enter a number : "))
count = 0
num = 2
while count<n :
    for i in range (2,num) :
        if num % i == 0 :
            break
    else :
        print(num,"\n")
    count = count +1
    num = num+1