"""
Write a function that determines whether or not a list of values is in sorted order (either ascending or descending).
The function should return True if the list is already sorted. Otherwise, it should return False. Write a main program
that reads a list of numbers from the user and then uses your function to report whether or not the list is sorted.
Make sure you consider these questions when completing this exercise: Is a list that is empty in sorted order?
What about a list containing one element?
"""
import math

def exercise_120(list):
  result = ""
  if len(list) == 1 or len(list) == 0:
    result = "List is too short to determine result"
  elif len(list) > 1:
    sliced_list = [int(list[i]) for i in range(len(list))]
    for i in range(0,math.floor(len(list) / 2),3):
      first_previous = sliced_list[i]
      second_previous = sliced_list[i + 1]
      third_previous = sliced_list[i + 2]
      fourth_previous = sliced_list[i + 3]
      if (first_previous > second_previous and second_previous > third_previous and third_previous > fourth_previous) or (first_previous < second_previous and second_previous < third_previous and third_previous < fourth_previous):
        pass
      else:
        result = "List is unsorted"
        return result
    first_previous = sliced_list[-1]
    second_previous = sliced_list[-2]
    third_previous = sliced_list[-3]
    if (first_previous > second_previous and second_previous > third_previous) or (first_previous < second_previous and second_previous < third_previous):
      result = "List is sorted"
    else:
      result = "list is unsorted"
  else:
    pass
  return result

"""
To run code:

from s3_exercises.exec120 import exercise_120 as exec120


num_list = []
user_input = int(input("Enter an integer: "))
while user_input != 0:
  num_list.append(user_input)
  user_input = int(input("Enter another integer: "))
print(exec120(num_list))
"""