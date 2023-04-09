"""
Write a program that computes the amount of gas in moles when the user supplies
the pressure, volume and temperature. Test your program by determining the number
of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
approximately 20 degrees Celsius or 68 degrees Fahrenheit.
"""

def calculate_gas_amt(gas_vol: float, pressure: float, temperature: float, temperature_type: str):
    GAS_CONSTANT = 8.314
    if temperature_type == "fahrenheit":
        temperature = (temperature - 32) * (5 / 9) + 273.15
    elif temperature_type == "celsius": 
        temperature += 273.15
    else:
        print("Error, invalid temperature format given")
    print(f"The amount of gas in moles is {(pressure * gas_vol) / (GAS_CONSTANT * temperature)} moles")