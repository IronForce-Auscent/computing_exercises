"""
In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0
"""

import sys
def exercise_61():
  total = 0
  count = 0
  value = int(input("Input a value: "))
  if value == 0:
    sys.exit("First input cannot be 0")
  while value != 0:
    total += value
    count += 1
    value = int(input("Input another value: "))
  if count == 0: average = 0
  else: average = total/count
  print(average)