"""
Write a program that prompts the user to enter a string with four letters and then
displays the string backwards. For example, if the string entered is "part", the program
must display "trap".
"""

def exercise_1():
  string = input("Input 4 letter string: ")[::-1]
  print(f"The reversed string is {string}")
    