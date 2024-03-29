"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
"""

def sum_intermediate_numbers(n: int):
  total = 0
  for i in range(1, n + 1):
    total += (i * (i + 1) / 2)
  print(total)