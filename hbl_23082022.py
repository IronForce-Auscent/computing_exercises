"""
Write a program that prompts the user to enter a string with four letters and then
displays the string backwards. For example, if the string entered is "part", the program
must display "trap".
"""

def exercise_1():
  print(f"The reversed string is {input('Input 4 letter string: ')[::-1]}")

"""
Write a program that prompts the user to enter a four-digit integer and then calculates
and outputs the sum of its digits. Use a For loop to complete this exercise. For example,
if the integer entered is "2023", the program must output "7".
"""
def exercise_2():
  digit = input("Input 4 digit integer: ")
  output = 0
  for i in range(4):
    output += int(digit[i])
  print(output)

"""
Write a program that prompts the user to enter his or her name and then creates and
prints a login ID from the first four letters of the name (in lowercase) and a four-digit
random integer. For example, if the name entered is 'Peter Parker', the program must
create and print a login ID which could be 'pete8041'.
"""
def exercise_3():
  import random
  name = input("Input user name: ")[:4:]
  random_int = random.randint(1, 9999)
  print(f"Your login ID is {name + str(random_int)}")

"""
Write a program that displays a random string consisting of five letters. For example,
the program may generate and display "invze".
"""
import random

def exercise_4():
  string = ""
  for i in range(5):
    string += chr(random.randint(97, 122))
  print(string)