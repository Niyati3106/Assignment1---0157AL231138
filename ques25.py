#Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once) using a for loop.
import string
str = input("Enter a string : ")
lower_set = set(string.ascii_lowercase)
str_set = set(str.lower())
if lower_set <= str_set :
      print("True")
else :
      print("False")