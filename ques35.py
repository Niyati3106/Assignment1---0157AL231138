#Write a program using a while loop to find the largest prime factor of a given number.
n = int(input("Enter a number : "))
i = n
while i>0 :
    if n%i == 0 :
        for j in range(2,i) :
            if i%j ==0 :
                break
        else :
            print(i," is the largest prime factor of ",n)
            i=0
    i = i-1