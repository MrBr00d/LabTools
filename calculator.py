def dilution():
  stock_concentration = float(input('Enter stock concentration here: ').replace(',', '.'))
  desired_concentration = float(input('Enter desired concentration here: ').replace(',', '.'))
  desired_volume = float(input('Enter desired volume here: ').replace(',', '.'))
  dilution_factor = desired_concentration / stock_concentration
  stock_calculation = dilution_factor * desired_volume
  dilutant_calculation = desired_volume - stock_calculation

  print(f'Stock volume to be added: {stock_calculation}.')
  print(f'Dilutant volume to be added: {dilutant_calculation}')
