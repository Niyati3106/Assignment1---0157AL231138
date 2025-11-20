'''Write a program to calculate electricity bill based on units:

Up to 100 units: ₹5 per unit,
101–200 units: ₹7 per unit,
Above 200 units: ₹10 per unit.'''

unit = int(input("Enter the total units : "))
bill =0
if unit>200 :
    unit = unit - 200
    bill = (unit*10) + (100*5) + (100*7)
elif unit>100 and unit<=200 :
    unit = unit - 100
    bill = (unit*7) + (100*5)
else :
    bill = unit * 5
print("Total bill = Rs",bill)  