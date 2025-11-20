#Write a program to assign grades based on marks:

#90-100: A,
#75-89: B,
#50-74: C,
#35-49: D,
#<35: Fail.

grade = int(input("Enter the marks : "))
if grade>=90 and grade<=100 :
    print("Grade = A")
elif grade>=75 and grade<=89 :
    print("Grade = B")
elif grade>=50 and grade<=74 :
    print("Grade = C")
elif grade>=35 and grade<=49 :
    print("Grade = D")   
else :
    print("Grade = fail")