"""
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
"""

def exercise_38():
  month = input("Enter a month: ").capitalize()
  days_31 = "January, March, May, July, August, October, December"
  days_30 = "April, June, September, November"
  if month in days_31:
    print("31 days")
  elif month in days_30:
    print("30 days")
  elif month == "Feburary":
    print("28 or 29 days")
  else:
    return 0