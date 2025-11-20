#Write a program using a for loop to print all Armstrong numbers between 100 and 999. (Armstrong number: sum of cubes of digits equals the number itself. Example: 153 => 13+53+33 = 153).
for i in range(100,1000) :
    temp = i
    sum = 0
    while temp>0 :
        rem = temp%10
        sum = sum + (rem**3)
        temp = temp//10
    if sum==i :
        print(i,"\n")