import calculator

print('1 = Stock dilution')
print('2 = Solution')
print('3 = (W%/V)')
choice = int(input("What action do you want to perform? "))

if choice == 1:
  calculator.dilution()
elif choice == 2:
  calculator.solution()
elif choice == 3:
  calculator.Weight_volume_percent()
else:
  print('No valid choice')
input("Press enter to exit.")
