"""
Write a function that takes three numbers as parameters and returns the median value of those parameters as its
result. Include a main program that reads three values from the user and displays their median.
"""

def exercise_84(nums): 
  smallest = 9999999999999999
  highest = 0
  num_list = [nums[i] for i in range(len(nums))]
  for i in range(len(num_list)):
    if num_list[i] > highest:
      highest = num_list[i]
    if num_list[i] < smallest:
      smallest = num_list[i]
  for num in num_list:
    if num != smallest and num != highest:
      return num


# Test 
"""
from s3_exercises.exec84 import exercise_84 as exec84
import random
num_list = []

def generate_numlist():
  global num_list
  for i in range(3):
    num_list.append(random.randint(0, 100000))
  return num_list
  

generate_numlist()
print(num_list)
print(exec84(num_list))
"""