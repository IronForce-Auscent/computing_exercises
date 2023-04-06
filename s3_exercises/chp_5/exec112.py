"""
Write a program that reads numbers from the user until a blank line is entered. Your
program should display the average of all of the values entered by the user. Then
the program should display all of the below average values, followed by all of the
average values (if any), followed by all of the above average values. An appropriate
label should be displayed before each list of values.
"""



def exercise_112():
  average = 0
  total = 0
  above_average = []
  below_average = []
  average_list = []
  integer_list = []
  integer = input("Enter an integer (blank line to quit): ")
  while integer == "":
    integer = input("First number cannot be a blank space. Please re-enter an integer: ")
  while integer != "":
    integer_list.append(int(integer))
    integer = input("Enter another integer (blank line to quit): ")
    total += int(integer)
  average = total / len(integer_list)
  for i in range(len(integer_list)):
    if float(integer_list[i]) < average:
      below_average.append(integer_list[i])
    elif float(integer_list[i]) > average:
      above_average.append(integer_list[i])
    else:
      average_list.append(integer_list[i])
  print(f"The average of the integers inputted is {average}")
  print(f"The values that are below average are {below_average}")
  print(f"The values that are average are {average_list}")
  print(f"The values that are average average are {above_average}")