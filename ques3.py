#Write a program to check if a given year is a leap year or not.
year = int(input("Enter the year : "))
if year%4==0  and year%100!=0 :
       print("Given year a leap year")
elif  year%100==0 and year%400==0  :
       print("Given year is a leap year")
else :
    print("Not a leap year")