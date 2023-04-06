"""
Write a program that reads integers from the user and stores them in a list. Your
program should continue reading values until the user enters 0. Then it should display
all of the values entered by the user (except for the 0) in order from smallest to largest,
with one value appearing on each line. Use either the sort method or the sorted
function to sort the list.
"""

def exercise_104():
  list_int = []
  exit = False
  int_input = int(input("Enter an integer here: "))
  while int_input == 0:
    int_input = int(input("First value cannot be a 0, please reenter an integer: "))
  list_int.append(str(int_input))
  while not exit:
    int_input = int(input("Enter another integer here: "))
    if int_input != 0:
      list_int.append(str(int_input))
    else:
      exit = True
  list_int.sort()
  for i in list_int:
    print(i)