"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized
"""

def exercise_15(ft: float):
    print(f"{ft} ft to inches: {ft * 12}")
    print(f"{ft} ft to yards: {ft / 3}")
    print(f"{ft} ft to miles: {ft / 5280}")