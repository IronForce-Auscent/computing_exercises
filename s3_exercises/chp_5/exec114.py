"""
In order to win the top prize in a particular lottery, one must match all 6 numbers on his or her ticket to the 6
numbers between 1 and 49 that are drawn by the lottery organizer. Write a program that generates a random
selection of 6 numbers for a lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates.
Display the numbers in ascending order.
"""

import random
def exercise_114():
  lottery_num = []
  for i in range(6):
    new_num = random.randint(1, 49)
    while new_num in lottery_num:
      new_num = random.randint(1, 49)
    lottery_num.append(new_num)
  lottery_num.sort()
  return lottery_num

"""
To run code:

from s3_exercises.exec114 import exercise_114 as exec114

print(exec114())
"""