"""
In this exercise you will create a program that reads a pressure from the user in kilopascals. Once the 
pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.
"""

def convert_from_pascals(air_pressure: float):
    PPSI, MOM, ATMOSPHERE = 6.895, 7.501, 101.3
    print(f"Air pressure in kilopascals: {air_pressure}")
    print(f"Converted to pounds per square inch: {air_pressure / PPSI}")
    print(f"Converted to millimeters of mercury: {air_pressure * MOM}")
    print(f"Converted to atmospheres: {air_pressure / ATMOSPHERE}")