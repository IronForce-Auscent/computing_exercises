"""
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet.
"""

def convert_from_celsius(temperature_celsius: float):
    print(f"Temperature: {temperature_celsius} Celsius")
    print(f"In Fahrenheit: {(temperature_celsius / 5 * 9) + 32}")
    print(f"In Kelvins: {temperature_celsius + 273.15}")