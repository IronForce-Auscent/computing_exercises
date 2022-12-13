"""
A prime number is an integer greater than 1 that is only divisible by one and itself. Write a function that determines
whether or not its parameter is prime, returning True if it is, and False otherwise. Write a main program that reads
an integer from the user and displays a message indicating whether or not it is prime. Ensure that the main program
will not run if the file containing your solution is imported into another program.
"""

def exercise_92(n):
  if n <= 3:
      return n > 1
  if n % 2 == 0 or n % 3 == 0:
      return False
  limit = int(n**0.5)
  for i in range(5, limit+1, 6):
      if n % i == 0 or n % (i+2) == 0:
        return False
  return True