"""
Mathematical expressions are often written in infix form, where operators appear between the operands on which
they act. While this is a common form, it is also possible to express mathematical expressions in postfix form,
where the operator appears after both operands. 

Use your solution to Exercise 122 to tokenize a mathematical expression. Then use the algorithm above to
transform the expression from infix form to postfix form. Your code that implements the preceding algorithm should
reside in a function that takes a list of tokens representing an infix expression as its only parameter. It should
return a list of tokens representing the equivalent postfix expression as its only result. Include a main program that
demonstrates your infix to postfix function by reading an expression from the user in infix form and displaying it in
postfix form.
The purpose of converting from infix form to postfix form will become apparent when you read Exercise 124. You
may find your solutions to Exercises 90 and 91 helpful when completing this problem. The algorithms provided in
Exercises 123 and 124 do not perform any error checking. As a result, you may crash your program or receive
incorrect results if you provide them with invalid input. These algorithms can be extended to detect invalid input and respond to it in a reasonable manner. Doing so is left as an independent study exercise for the interested
student.
"""

def exercise_123():
  to_pass = input("Enter a mathematical expression: ")
  result = removeTokens(to_pass)
  return convert(removeTokens(result))

def convert(string):
  operators = []
  postfix = []
  infix = [string[i] for i in range(len(string))]
  #infix = string.split()
  print(infix)
  for char in infix:
    print(char)
    print(operators)
    print(postfix)
    if str(char).isnumeric():
      postfix.append(char)
    if char in operators:
      while len(operators) != 0 and operators[-1] != "(" and operators.index(char) < operators.index(operators[-1]):
        postfix.append(operators.pop[-1])
      operators.append(char)
    if char == "(":
      operators.append(char)
    if char == ")":
      while operators[-1] != "(":
        postfix.append(operators.pop[-1])
      del operators[operators.index("(")]
  while len(operators) != 0:
    postfix.append(operators.pop(-1))
  return postfix


# Taken from exec122.py and modified
def removeTokens(string):
  tokens = ["*", "/", "^", "(", ")"]
  sliced_string = [string[i] for i in range(len(string))]
  final_string = []
  #substring = ""
  for char in sliced_string:
    """
    if char == "+" or char == "-":
      previous = sliced_string[(sliced_string.index(char) - 1)]
      if previous.isnumeric() or previous == ")" or previous.isspace():
        final_string.append(substring)
        substring = ""
      else:
        substring += char
    """
    if char.isspace():
      pass
    elif char in tokens:
      pass
    else:
      final_string.append(char)
  for item in final_string:
    if item == "":
      index = final_string.index(item)
      del final_string[index]
  return final_string