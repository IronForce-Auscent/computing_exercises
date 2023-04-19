'''
A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:
area = n × s2
4 × tan π
n

Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values.
'''

import math
def calculate_polygon_area(s: int, n: int):
  print(f"The area of the polygon with {n} sides is " + str((n * (s ** 2)) / 4 * math.tan(math.pi / n)))