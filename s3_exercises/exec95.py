"""In a particular jurisdiction, older license plates consist of three letters followed by three numbers. When all of the
license plates following that pattern had been used, the format was changed to four numbers followed by three
letters. Write a function that generates a random license plate. Your function should have approximately equal
odds of generating a sequence of characters for an old license plate or a new license plate. Write a main program
that calls your function and displays the randomly generated license plate."""
import random

def exercise_95():
  old_new = random.randint(0, 1)
  license = ""
  if old_new == 0:
    for i in range(3):
      license += chr(random.randint(65, 90))
    for i in range(3):
      license += str(random.randint(0, 9))
  else:
    for i in range(4):
      license += str(random.randint(0, 9))
    for i in range(3):
      license += chr(random.randint(65, 90))
  return license