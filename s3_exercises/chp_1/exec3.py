"""
Write a program that prompts the user to enter his or her name and then creates and
prints a login ID from the first four letters of the name (in lowercase) and a four-digit
random integer. For example, if the name entered is 'Peter Parker', the program must
create and print a login ID which could be 'pete8041'.
"""
def exercise_3():
  import random
  name = input("Input user name: ")[:4:]
  random_int = random.randint(0, 999)
  print(f"Your login ID is {name + str(random_int)}")