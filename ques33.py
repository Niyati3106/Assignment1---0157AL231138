#Write a program using a while loop to check whether a number is a Duck number (a number containing zero but not starting with zero, e.g., 202, 1203).
n = int(input("Enter a number : "))    
str_n = str(n)
i = 0
while i<len(str_n) :
    if str_n[i]=='0' :
        print(n, " is a duck number")
        break
    i=i+1
else :    
    print(n, " is not a duck number")