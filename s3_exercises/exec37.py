"""
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message
"""

def exercise_37():
  sides = int(input("Enter number of sides: "))
  if sides == 3: print("That shape is a triangle or trigon")
  if sides == 4: print("That shape is a quadrilateral or tetragon")
  if sides == 5: print("That shape is a pentagon")
  if sides == 6: print("That shape is a hexagon")
  if sides == 7: print("That shape is a heptagon")
  if sides == 8: print("That shape is an octagon")
  if sides == 9: print("That shape is a nonagon or enneagon")
  if sides == 10: print("That shape is a decagon")