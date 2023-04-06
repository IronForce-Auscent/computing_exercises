"""
Write a program that reads integers from the user and stores them in a list. Use 0 as a sentinel value to mark the
end of the input. Once all of the values have been read your program should display them (except for the 0) in
reverse order, with one value appearing on each line.
"""

def exercise_105():
  user_input = int(input("Enter an integer: "))
  input_list = []
  while user_input != 0:
    input_list.append(user_input)
    user_input = int(input("Enter another integer: "))
  return input_list