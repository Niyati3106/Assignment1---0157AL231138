#Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.
for num in range(1,501) :
    sum = 0
    if num%3==0 :
        temp=num
        while temp>0 :
            rem = temp%10
            sum = sum+rem
            temp=temp//10
        if sum<=10 :
            print(num,"\n")