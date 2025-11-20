#Write a program using a while loop to accept a number and check whether it is a Kaprekar number.
#(Kaprekar number: if square of the number can be split into two parts whose sum equals the number.
#Example: 452=2025 => 20+25=45).

n = int(input("Enter a number : "))
sq = n**2
sq_str = str(sq)
if len(sq_str)%2==0 :
    str1 = sq_str[:(len(sq_str)//2)]
    str2 = sq_str[(len(sq_str)//2):]
    n1 = int(str1)
    n2 = int(str2)
    if n1+n2 == n:
        print(n," is a kaprekar number")
    else :
        print(n," is not a kaprekar number")
else :
        print(n," is not a kaprekar number")