"""
In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
"""

def fuel_efficiency_calculator():
  conversion = 235.215
  mpg = int(input("Input fuel efficiency (in miles per galleon): "))
  print("The fuel efficiency (converted to litres per 100km) is " + str(conversion / mpg))
  #return (conversion / mpg)