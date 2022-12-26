"""
A proper divisor of a positive integer, n, is a positive integer less than n which divides evenly into n. Write a function
that computes all of the proper divisors of a positive integer. The integer will be passed to the function as its only
parameter. The function will return a list containing all of the proper divisors as its only result. Complete this
exercise by writing a main program that demonstrates the function by reading a value from the user and displaying
the list of its proper divisors. Ensure that your main program only runs when your solution has not been imported
into another file.
"""

def exercise_109(positive_int):
  divisor = 1
  proper_divisor = []
  while divisor < positive_int:
    if (positive_int % divisor) == 0:
      proper_divisor.append(divisor)
    divisor += 1
  return proper_divisor


"""
To run code:

from s3_exercises.exec109 import exercise_109 as exec109

userinput = int(input("Enter a positive integer: "))
print(exec109(userinput))
"""