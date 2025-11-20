
'''Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).'''


bmi = float(input("Enter the bmi : "))
if bmi<=0 :
    print("Enter a valid value")
elif bmi<=18.5 and bmi>0 :
    print("Underweight")
elif bmi>18.5 and bmi<=24.9 :
    print("Normal")
elif bmi>=25 and bmi<=29.9 :
    print("Overweight")
else :
    print("Obese")