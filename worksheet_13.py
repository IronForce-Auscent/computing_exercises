# Question 6
def timer():
  i = 21
  while i > 0:
    print(i - 1)
    i -= 1
  print("End of while loop")

# Question 7
def var_timer(var):
  for i in range(v):
    print("Your mom")
  print("Completed")

# Question 8:
def multiplication_table():
  selection = int(input("Which multiplication table do you want? "))
  for i in range(1, 10):
    print(f'{selection} x {i} = {selection * 1}')

# Question 9
def calc_factorial():
  fact = int(input("Which factorial do you want? "))
  result = 1
  while fact > 1:
    result *= fact
    fact -= 1
  print(result)

# Question 10
def validate_check(isbn):
  if len(isbn) != 9 or not isbn.isnumeric() or isbn.isspace() or isbn == Null:
    return True
  else:
    return False

def generate_isbn_check():
  isbn_first9 = input("Input the first 9 digits of an ISBN number: ")
  while validate_check(isbn_first9):
    isbn_first9 = input("Input a valid 9-digit ISBN number: ")
  isbn_char = [int(isbn_first9[i]) for i in range(9)]
  total = 0
  check_digit = 0
  for i in range(9):
    total += (isbn_char[i] * (10 - i))
  remainder = total % 11
  if remainder == 0:
    print("The check digit is 0")
  else:
    check_digit = 11 - remainder
  if check_digit != 10:
    print(f"The check digit is {check_digit}")
  else:
    print("The check digit is 'X'")
  print(f"The ISBN number is {isbn_first9 + str(check_digit)}")