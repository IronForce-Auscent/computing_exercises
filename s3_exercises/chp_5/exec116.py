"""
Extend your solution to Exercise 115 so that it correctly handles uppercase letters and punctuation marks such as
commas, periods, question marks and exclamation marks. If an English word begins with an uppercase letter then
its Pig Latin representation should also begin with an uppercase letter and the uppercase letter moved to the end
of the word should be changed to lowercase. For example, Computer should become Omputercay. If a word ends
in a punctuation mark then the punctuation mark should remain at the end of the word after the transformation has
been performed.
For example, Science! should become Iencescay!
"""

def exercise_116(string):
  vowel = ['a', 'e', 'i', 'o', 'u']
  result = ""
  original = [string[i] for i in range(len(string))]
  sliced_string = [string[i] for i in range(len(string))]
  if sliced_string[0] not in vowel:
    before_vowel = []
    for char in sliced_string:
      if char not in vowel:
        before_vowel.append(char.lower())
      else:
        break
    del sliced_string[:(len(before_vowel) - 1)]
    sliced_string.pop(0)
    for char in before_vowel:
      sliced_string.extend(char)
    sliced_string.extend(['a', 'y'])
    return capitalize_firstl(original, convert_to_string(sliced_string))
  elif sliced_string[0] in vowel:
    result = convert_to_string(sliced_string)
    result += "way"
    return capitalize_firstl(sliced_string, result)

def convert_to_string(to_convert):
  result = ""
  for char in to_convert:
    result += char

  return result

def capitalize_firstl(original, new):
  if original[0].isupper():
    new.lower()
    return new.capitalize()
  else:
    return new


"""
from s3_exercises.exec116 import exercise_116 as exec116


input_string = input("Please enter a string: ")
print(exec116(input_string))
"""