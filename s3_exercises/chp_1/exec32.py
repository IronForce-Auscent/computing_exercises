'''
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
'''

def sort_by_largest(list_input: list):
  print("The largest integer is " + str(max(list_input)))
  print("The smallest integer is " + str(min(list_input)))
  print("The middle number is " + str(sum(list_input) - max(list_input) - min(list_input)))