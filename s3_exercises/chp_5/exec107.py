"""
In this exercise, you will create a program that reads words from the user until the
user enters a blank line. After the user enters a blank line your program should display each word entered by the user exactly once. The words should be displayed in
the same order that they were entered.
"""


def exercise_107():
  words = []
  word = input("Enter a word (blank line to quit): ")
  while not word == "":
    flag = False
    if word in words:
      flag = True
    else:
      words.append(word)
    word = input("Enter another word (blank line to quit): ")
  print(words)