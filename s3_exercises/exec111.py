"""
In this exercise you will create a program that identifies all of the words in a string entered by the user. Begin by
writing a function that takes a string of text as its only parameter. Your function should return a list of the words in
the string with the punctuation marks at the edges of the words removed. The punctuation marks that you must
remove include commas, periods, question marks, hyphens, apostrophes, exclamation points, colons, and
semicolons. Do not remove punctuation marks that appear in the middle of a words, such as the apostrophes used
to form a contraction. For example, if your function is provided with the string "Examples of contractions include:
don’t, isn’t, and wouldn’t." then your function should return the list ["Examples", "of", "contractions", "include",
"don’t", "isn’t", "and", "wouldn’t"]. Write a main program that demonstrates your function. It should read a string
from the user and display all of the words in the string with the punctuation marks removed. You will need to import
your solution to this exercise when completing Exercise 158. As a result, you should ensure that your main program
only runs when your file has not been imported into another program.
"""

def exercise_111(string):
  punctuation = [",", ".", "?", "!", ":", ";"]
  filtered = []
  sliced_string = string.split()
  print(sliced_string)
  for word in sliced_string:
    print(word)
    if any(punc in word for punc in punctuation):
      # Slice the word up into its characters
      sliced_word = [word[i] for i in range(len(word))]
      new_word = ""
      for char in sliced_word:
        if char in punctuation:
          pass
        else:
          new_word += char
          print(new_word)
      filtered.append(new_word)
    elif "’" in word or "-" in word:
      # Check if the apostrophe is stand-alone
      if len(word) > 1:
        filtered.append(word)
      else:
        pass
    else:
      filtered.append(word)

  return filtered
  

"""
To run code:

from s3_exercises.exec111 import exercise_111 as exec111


user_input = input("Please enter a string: ")
print(exec111(sample_text))
"""