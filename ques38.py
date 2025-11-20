#Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even=> n/2, if odd => 3n+1. Continue until n=1).
n = int(input("Enter a number : "))
print(n)
while n!=1 :
    if n%2==0 :
        n=n//2
        print(n)
    else :
        n=(3*n)+1
        print(n)