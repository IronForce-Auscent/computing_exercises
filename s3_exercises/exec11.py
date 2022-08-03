'''
In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
'''

def exercise_11():
  conversion = 235.215
  mpg = float(input("Insert fuel effiency value here (MPG): "))
  print("Fuel efficiency (converted to litres per 100km): " + str(conversion / mpg))