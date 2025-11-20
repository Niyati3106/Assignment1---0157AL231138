#Write a program to check if a given year is a century year and also a leap year.
year = int(input("Enter the year : "))
if year%100 ==0 :
    if year%400==0 :
        print("Year is a century and a leap year")
    else :
        print("Year is a century but not a leap year")
else :
    print("Year is not a century")