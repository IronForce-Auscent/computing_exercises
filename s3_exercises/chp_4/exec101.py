"""
Write a function that takes two positive integers that represent the numerator and denominator of a fraction as its
only two parameters. The body of the function should reduce the fraction to lowest terms and then return both the
numerator and denominator of the reduced fraction as its result. For example, if the parameters passed to the
function are 6 and 63 then the function should return 2 and 21. Include a main program that allows the user to
enter a numerator and denominator. Then your program should display the reduced fraction.
Hint: In Exercise 75 you wrote a program for computing the greatest common divisor of two positive integers. You
may find that code useful when completing this exercise.
"""

def exercise_101(num, den):
  d = num if num < den else den
  while num % d != 0 or den % d != 0:
    d -= 1
  num /= d
  den /= d
  print(f"{num}/{den}")