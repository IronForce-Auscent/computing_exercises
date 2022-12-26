"""
An integer, n, is said to be perfect when the sum of all of the proper divisors of n is equal to n. For example, 28 is
a perfect number because its proper divisors are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28. Write a function
that determines whether or not a positive integer is perfect. Your function will take one parameter. If that parameter
is a perfect number then your function will return true. Otherwise, it will return false. In addition, write a main
program
that uses your function to identify and display all of the perfect numbers between 1 and 10,000. Import your solution
to Exercise 109 when completing this task.
"""

def exercise_110(n):
  divisor = 1
  proper_divisor = []
  while divisor < n:
    if (n % divisor) == 0:
      proper_divisor.append(divisor)
    divisor += 1
  sum = 0
  for i in range(len(proper_divisor)):
    sum += proper_divisor[i]
  if sum == n:
    return True
  else:
    return False


"""
To run code:

from s3_exercises.exec110 import exercise_110 as exec110

perfect = []
for i in range(1, 1000):
  result = exec110(i)
  if result == True:
    perfect.append(i)

print(perfect)
"""