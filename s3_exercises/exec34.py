'''
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.
'''
def exercise_34():
  user_input = int(input("Input a positive integer: "))
  if user_input % 2 == 0:
    print("The input is an even number")
  else:
    print("The input is an odd number")
    