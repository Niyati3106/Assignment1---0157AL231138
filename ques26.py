#Write a program using a for loop to print all twin primes between 1 and 100. (Twin primes: pairs of prime numbers with a difference of 2, e.g., (3,5), (11,13)).
prev =-1
curr =-1
for i in range(2,101) :
    for j in range(2,i) :
        if i%j==0 :
            break
    else :
        prev = curr
        curr = i
        if curr-prev==2 :
           print(prev,",",curr)