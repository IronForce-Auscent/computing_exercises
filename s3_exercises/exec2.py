"""
Write a program that prompts the user to enter a four-digit integer and then calculates
and outputs the sum of its digits. Use a For loop to complete this exercise. For example,
if the integer entered is "2023", the program must output "7".
"""

def exercise_2():
  integer_4d = int(input("Input 4 digit integer: "))
  total = 0
  for i in range(4):
    total += (integer_4d % (10 * (i + 1)))
  print(str(total))