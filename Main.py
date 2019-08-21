import calculator
import os

print('1 = Stock dilution')
print('2 = NA')
choice = int(input("What action do you want to perform? "))

if choice == 1:
  os.system('cls')
  calculator.dilution()
else:
  print('No valid choice')
input("Press enter to exit.")
