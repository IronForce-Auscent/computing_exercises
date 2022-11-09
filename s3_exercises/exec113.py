"""
Write a function that takes a list of strings as its only parameter. Your function
should return a string that contains all of the items in the list formatted in the manner
described previously as its only result. While the examples shown previously only
include lists containing four elements or less, your function should behave correctly
for lists of any length. Include a main program that reads several items from the user,
formats them by calling your function, and then displays the result returned by the
function.
"""


def exercise_113(string_list):
  output_list = ""
  length = 0
  if len(string_list) == 1:
    return string_list[0]
  if len(string_list) == 2:
    return string_list[0] + " and " + string_list[1]

  for word in range(len(string_list) - 2):
    output_list += string_list[word] + ", "
  output_list += string_list[-2] + " and " + string_list[-1]
  return output_list

def main():
  string_count = int(input("Input number of string: "))
  string_list = []
  for word in range(string_count):
    string = input("Input a string: ")
    while string == "":
      string = input("String cannot be a blank line. Please enter a valid string: ")
    string_list.append(string)
  print(exec113(string_list))