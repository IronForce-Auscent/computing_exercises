"""
Write a program that displays a random string consisting of five letters. For example,
the program may generate and display "invze".
"""
import random

def exercise_4():
  string = ""
  for i in range(4):
    string += chr(random.randint(97, 122))
  print(string)