"""
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
"""
import math
def exercise_16():
  r = int(input("Input radius of circle: "))
  print(f"The area of the circle with a radius of {r} is " + str(math.pi * (r ** 2)))
  print(f"The volume of a sphere with a radius of {r} is " + str((4 / 3) * math.pi * (r ** 3)))