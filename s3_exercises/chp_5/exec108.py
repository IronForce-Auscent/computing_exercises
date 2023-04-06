"""
Create a program that reads integers from the user until a blank line is entered. Once
all of the integers have been read your program should display all of the negative
numbers, followed by all of the zeros, followed by all of the positive numbers. Within
each group the numbers should be displayed in the same order that they were entered by the user.
"""

def exercise_108():
  final = []
  positive = []
  negative = []
  zero = []
  integer = input("Enter an integer: ")
  
  while integer != "":
    if int(integer) < 0:
      negative.append(int(integer))
    elif int(integer) > 0:
      positive.append(int(integer))
    else:
      zero.append(0)
    integer = input("Enter another integer: ")
  for n in range(len(negative)):
    final.append(negative[n])
  for i in range(len(zero)):
    final.append(zero[i])
  for p in range(len(positive)):
    final.append(positive[p])
  print(final)