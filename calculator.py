def dilution():
  stock_concentration = float(input('Enter stock concentration here: ').replace(',', '.'))
  desired_concentration = float(input('Enter desired concentration here: ').replace(',', '.'))
  desired_volume = float(input('Enter desired volume here: ').replace(',', '.'))
  dilution_factor = desired_concentration / stock_concentration
  stock_calculation = dilution_factor * desired_volume
  dilutant_calculation = desired_volume - stock_calculation

  print(f'Stock volume to be added: {stock_calculation}.')
  print(f'Dilutant volume to be added: {dilutant_calculation}')

def solution():
  desired_volume = float(input("Enter desired volume (L): "))
  desired_concentration = float(input("Enter desired concentration (M): "))
  molar_weight = float(input("Enter molar weight of substance (g/mol): "))
  calculation = desired_volume * desired_concentration * molar_weight
  print(f"Mass of substance to add: {calculation} g")

def Weight_volume_percent():
  desired_wv = float(input("Desired % W/V :").replace(",", "."))
  desired_volume = float(input("Desired volume (mL) :").replace(",", "."))
  
  calculation = desired_wv * desired_volume / 100
  
  print("Mass of solute needed (g): ", calculation, "g")
