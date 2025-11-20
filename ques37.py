#Write a program using a while loop to compute the sum of digits of a number until the result becomes a single-digit number (Digital root). Example: 9875 => 9+8+7+5=29 => 2+9=11 => 1+1=2.
n = int(input("Enter a number : "))
sum = 0
temp = n
while temp>=10 :
    
    while temp>0 :
        rem=temp%10
        sum = sum+rem
        temp = temp//10
    if sum>=10 :
        temp = sum
        sum=0
print("Sum = ",sum)   