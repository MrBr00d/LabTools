import calculator
import os

print('1 = Stock dilution')
print('2 = Solution')
choice = int(input("What action do you want to perform? "))

if choice == 1:
  os.system('cls')
  calculator.dilution()
elif choice == 2:
  os.system('cls')
  calculator.solution()
else:
  print('No valid choice')
input("Press enter to exit.")
