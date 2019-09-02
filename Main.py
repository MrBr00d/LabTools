import calculator
import os

def menu():
  print('1 = Stock dilution')
  print('2 = Solution')
  print('3 = (W%/V)')
  choice = int(input("What action do you want to perform? "))

  if choice == 1:
    os.system('cls')
    calculator.dilution()
  elif choice == 2:
    os.system('cls')
    calculator.solution()
  elif choice == 3:
    os.system('cls')
    calculator.Weight_volume_percent()
  else:
    print('No valid choice')
  again()

def again():
  print("Do you want to run the calculator again?")
  print('1 = Yes')
  print('2 = No')

  choice = int(input())

  if choice == 1:
    os.system('cls')
    menu()
  else:
    pass

menu()
