"""
In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.
"""
def exercise_36(letter: str):
  vowels = ["a", "e", "i", "o", "u"]
  if letter.lower() in vowels: print(f"The letter {letter} is an alphabet")
  if letter.lower() == "y": print(f"The letter {letter} can sometimes be a vowel, and other times be a consonant")
  else: print(f"The letter {letter} is a consonant")