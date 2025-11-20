
# Write a program to simulate an ATM machine using a while loop where a user can:
#• Check balance
#• Deposit money
#• Withdraw money (only if balance is sufficient)
#• Exit
#Continue until the user chooses to exit.

balance = 1000
op = input("Enter the operation : ")
while op!="exit" :
      if op=="check balance" :
          print("Balance : ",balance)
      elif op=="deposit money" :
          money = int(input("Enter amount : "))
          balance = balance + money
          print("Balance : ",balance)
      elif op=="withdraw money" :
          money = int(input("Enter amount : "))
          if money>balance :
              print("Insufficient balance")
          else :
              balance = balance - money
              print("Balance : ",balance)
      op = input("Enter the operation : ")