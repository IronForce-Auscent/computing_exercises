"""Many people do not use capital letters correctly, especially when typing on small devices like smart phones. In this
exercise, you will write a function that capitalizes the appropriate characters in a string. A lowercase “i” should be
replaced with an uppercase “I” if it is both preceded and followed by a space. The first character in the string
should also be capitalized, as well as the first non-space character after a “.”, “!” or “?”. For example, if the function
is provided with the string “what time do i have to be there? what’s the address?” then it should return the string
“What time do I have to be there? What’s the address?”. Include a main program that reads a string from the user,
capitalizes it using your function, and displays the result.
"""

def exercise_89(string):
  sliced_string = [string[i] for i in range(len(string))]
  next_cap = [".", "?", "!"]
  new_string = ""
  for i in range(len(sliced_string)):
    if i == 0:
      new_string += sliced_string[i].upper()
    else:
      if i > 0 and (sliced_string[i - 1] in next_cap or (sliced_string[i - 2] in next_cap and sliced_string[i - 1].isspace())):
        new_string += sliced_string[i].upper()
      else:
        if sliced_string[i - 1].isspace() and sliced_string[i + 1].isspace() and sliced_string[i] == "i":
          new_string += sliced_string[i].upper()
        else:
          new_string += sliced_string[i]
  return new_string