"""
In this exercise you will create a function named nextPrime that finds and returns the first prime number larger
than some integer, n. The value of n will be passed to the function as its only parameter. Include a main program
that reads an integer from the user and displays the first prime number larger than the entered value. Import and
use your solution to Exercise 92 while completing this exercise.
"""

def exercise_93(n):
  i = n + 1
  while True:
    if is_prime(n):
      return i
    i += 1
    
def is_prime(n):
  i =2
  while i <= (n/2):
    if n % i != 0:
      i += 1
    else:
      return False
  return True