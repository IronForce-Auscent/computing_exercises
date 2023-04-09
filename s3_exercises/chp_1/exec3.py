"""
Write a program that prompts the user to enter his or her name and then creates and
prints a login ID from the first four letters of the name (in lowercase) and a four-digit
random integer. For example, if the name entered is 'Peter Parker', the program must
create and print a login ID which could be 'pete8041'.
"""
def create_login_id(name: str):
  import random
  response = name[:4]
  for i in range(4):
    response += random.randint(0, 9)
  print(response)