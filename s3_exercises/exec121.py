"""
Python’s standard library includes a method named count that determines how many times a specific value occurs
in a list. In this exercise, you will create a new function named countRange which determines and returns the
number of elements within a list that are greater than or equal to some minimum value and less than some
maximum value. Your function will take three parameters: the list, the minimum value and the maximum value. It
will return an integer result greater than or equal to 0. Include a main program that demonstrates your function for
several different lists, minimum values and maximum values. Ensure that your program works correctly for both
lists of integers and lists of floating point numbers.
"""

def exercise_121(list, min_v, max_v):
  return countRange(list, min_v, max_v)

def countRange(list, min_v, max_v):
  over_max = []
  below_min = []
  for num in list:
    if num > max_v:
      over_max.append(num)
    if num <= min_v:
      below_min.append(num)
  return over_max, below_min


"""
To run code:

from s3_exercises.exec121 import exercise_121 as exec121

input_list = []
user_input = float(input("Enter a floating-point/integer value: "))
while user_input != 0:
  input_list.append(user_input)
  user_input = float(input("Enter another value: "))
max_num = float(input("Enter a maximum value: "))
min_num = float(input("Enter a minimum value: "))
result = exec121(input_list, min_num, max_num)
print(f"Numbers over the max: {result[0]}")
print(f"Numbers equal to or below the min: {result[1]}")
"""