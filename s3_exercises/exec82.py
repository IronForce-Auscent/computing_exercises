"""
In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters traveled. Write
a function that takes the distance traveled (in kilometers) as its only parameter and returns the total fare as its only
result. Write a main program that demonstrates the function.
"""

def exercise_82(distance):
  return 4 + ((distance / .14) * .25)