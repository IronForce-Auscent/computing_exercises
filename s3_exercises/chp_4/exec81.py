"""
Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
theorem, as the function’s result. Include a main program that reads the lengths of
the shorter sides of a right triangle from the user, uses your function to compute the
length of the hypotenuse, and displays the result.
"""


import math
def exercise_81():
  hypo = math.sqrt(math.pow(base, 2) + math.pow(height, 2))
  return hypo

base = float(input("Enter length of the triangle: "))
height = float(input("Enter height of the triangle: "))
print(exercise_81())