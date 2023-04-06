"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
"""
from math import pi, pow

def exercise_18(radius: float, height: float):
    return round(pi * pow(radius, 2) * height)