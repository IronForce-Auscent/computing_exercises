"""
Write a function that determines how many days there are in a particular month. Your function will take two
parameters: The month as an integer between 1 and 12, and the year as a four-digit integer. Ensure that your
function reports the correct number of days in February for leap years. Include a main program that reads a month
and year from the user and displays the number of days in that month. You may find your solution to Exercise 57
helpful when solving this problem.
"""

def exercise_100(month, year):
  month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
  leap = False
  if year % 4 == 0:
    leap = True
  else:
    leap = False
  if month == 2 and leap == True:
    return 29
  else:
    return month_days[month]

"""
Execution of code:

from s3_exercises.exec100 import exercise_100 as exec100


year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))
print(exec100(month, year))
"""