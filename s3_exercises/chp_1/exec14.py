"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
"""

def imperial_to_metric(ft: float, inch: float):
    print(f"{ft} feet and {inch} inch(es) to {ft * 30.48 + inch * 2.54} cm")