"""In this exercise you will write a function that determines whether or not a password is good. We will define a good
password to be a one that is at least 8 characters long and contains at least one uppercase letter, at least one
lowercase letter, and at least one number. Your function should return true if the password passed to it as its only
parameter is good. Otherwise, it should return false. Include a main program that reads a password from the user
and reports whether or not it is good. Ensure that your main program only runs when your solution has not been
imported into another file.
"""

def exercise_96(password):
  if len(password) < 8:
    return "Weak password"
  else:
    password_split = [password[i] for i in range(len(password))]
    lowercase = 0
    uppercase = 0
    one_num = 0
    for char in password_split:
      if char.isupper():
        uppercase = 1
      if char.islower():
        lowercase = 1
      if char.isnumeric():
        one_num = 1
    if lowercase == 1 and uppercase == 1 and one_num == 1: 
      return "Strong password"
    else:
      return "Weak password"