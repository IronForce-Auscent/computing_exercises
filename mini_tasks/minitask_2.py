import random

word_list = ['yes', 'but', 'no', 'henceforth', 'therefore', 'your mom']
prompt = "Start guessing an animal"
split_word = []

def check_guess(guess):
  global split_word
  while game_continue:
    if guess_count < max_guess:
      if 
  for i in range(len(split_word)):
    if split_word[i] == guess:
      return i
    else:
      return -1

def initialize():
  global split_word
  selected_word = word_list[random.randint(0, len(word_list))]
  split_word = selected_word.split()

def game_start():
  print(prompt)
  array = ""
  for i in range(len(split_word)):
    array += "_ "
  print(array)