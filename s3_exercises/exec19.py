'''
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s2. You can use the formula vf2 = v2i + 2ad to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.
'''

import math
def exercise_19():
  height = int(input("Input initial height of object: "))
  print("The speed of the object travelling when it hits the ground is " + str(math.sqrt((0 ** 2) + 2 * 9.8 * height)))