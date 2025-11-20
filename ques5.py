#Write a program to check whether a person is eligible to vote (age >= 18).
age = int(input("Enter your age : "))
if age <= 0 :
    print("Enter valid age")
elif age >=18 :
    print("Eligible for voting")
else :
    print("Not eligible for voting")