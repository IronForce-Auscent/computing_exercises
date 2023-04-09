'''
Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3+1+4+1=9.
'''

def sum_digits(int_input: int):
  output = 0
  x = [int(a) for a in str(int_input)]
  for i in range(4):
    output += x[i]
  print(output)