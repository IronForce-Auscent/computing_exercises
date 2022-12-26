"""
When analysing data collected as part of a science experiment it may be desirable to remove the most extreme
values before performing other calculations. Write a function that takes a list of values and an non-negative integer,
n, as its parameters. The function should create a new copy of the list with the n largest elements and the n
smallest elements removed. Then it should return the new copy of the list as the function’s only result. The order
of the elements in the returned list does not have to match the order of the elements in the original list. Write a
main program that demonstrates your function. Your function should read a list of numbers from the user and
remove the two largest and two smallest values from it. Display the list with the outliers removed, followed by the
original list. Your program should generate an appropriate error message if the user enters less than 4 values.
"""

def exercise_106(value_list, n):
  value_list.sort()
  if len(value_list) > 4:
    new_list = value_list[:n]
    return new_list
  else:
    print("List should contain more than 4 values")


"""
To run code:

from s3_exercises.exec106 import exercise_106 as exec106


value_list = []
value_input = input("Enter a value: ")
while value_input != "0":
  value_list.append(value_input)
  value_input = input("Enter another value: ")
n = int(input("Enter a non-negative integer: "))
print(exec106(value_list, n))
"""