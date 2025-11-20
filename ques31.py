#Write a program using a while loop to find the reverse of a number and check if the reversed number is prime. Example: Input = 73 → Reverse = 37 → Prime.
n = int(input("Enter a number : "))
temp = n
rev = 0
while temp > 0 :
    rem = temp%10
    rev = rev*10 + rem
    temp = temp//10
i = 2
while i<rev :
    if rev%i == 0 :
        print("Reverse of ",n," is not prime")
        break
    else :
        i=i+1
else :    
    print("Reverse of ",n," is prime : ",rev)