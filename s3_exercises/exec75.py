"""
The greatest common divisor of two positive integers, n and m, is the largest number,
d, which divides evenly into both n and m. There are several algorithms that can be
used to solve this problem, including:
Initialize d to the smaller of m and n.
While d does not evenly divide m or d does not evenly divide n do
Decrease the value of d by 1
Report d as the greatest common divisor of n and m
Write a program that reads two positive integers from the user and uses this algorithm
to determine and report their greatest common divisor.
"""

def exercise_75(n1, n2):
  d = n1 if n1 < n2 else n2
  while n1 % d != 0 or n2 % d != 0:
    d -= 1
  return d