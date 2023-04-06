'''
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a^b
'''

import math
def exercise_10():
  a = int(input("Enter integer a: "))
  b = int(input("Enter integer b: "))
  print("The sum is " + str((a + b)))
  print("The difference is " + str((a - b)))
  print("The product is " + str((a * b)))
  print("The quotient is " + str((a // b)))
  print("The remainder is " + str((a % b)))
  print(f"The result of {a} to the power of {b} is " + str((a ** b)))
  print(f"The result of lg {a} is " + str(math.log(a, 10)))