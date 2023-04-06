"""
Pig Latin is a language constructed by transforming English words. While the origins of the language are unknown,
it is mentioned in at least two documents from the nineteenth century, suggesting that it has existed for more than
100 years. The following rules are used to translate English into Pig Latin:
• If the word begins with a consonant (including y), then all letters at the beginning of the word, up to the first vowel
(excluding y), are removed and then added to the end of the word, followed by ay. For example, computer becomes
omputercay and think becomes inkthay.
• If the word begins with a vowel (not including y), then way is added to the end of the word. For example, algorithm
becomes algorithmway and office becomes officeway.
Write a program that reads a line of text from the user. Then your program should translate the line into Pig Latin
and display the result. You may assume that the string entered by the user only contains lowercase letters and
spaces.
"""

def exercise_115(string):
  vowel = ['a', 'e', 'i', 'o', 'u']
  sliced_string = [string[i] for i in range(len(string))]
  if sliced_string[0] not in vowel:
    before_vowel = []
    for char in sliced_string:
      if char not in vowel:
        before_vowel.append(char)
      else:
        break
    del sliced_string[:(len(before_vowel) - 1)]
    sliced_string.pop(0)
    for char in before_vowel:
      sliced_string.extend(char)
    sliced_string.extend(['a', 'y'])
    return convert_to_string(sliced_string)
  elif sliced_string[0] in vowel:
    result = convert_to_string(sliced_string)
    result += "way"
    return result

def convert_to_string(to_convert):
  result = ""
  for char in to_convert:
    result += char

  return result