"""
Write a program that displays a random string consisting of five letters. For example,
the program may generate and display "invze".
"""
import random

def generate_random_string():
  response = ""
  for i in range(4):
    response += chr(random.randint(97, 122))
  print(response)