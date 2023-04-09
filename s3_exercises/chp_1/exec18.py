"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
"""
from math import pi, pow

def calculate_cylinder_volume(radius: float, height: float):
    print(f"The volume of the cylinder is {round(pi * pow(radius, 2) * height)} units cubed")