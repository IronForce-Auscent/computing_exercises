"""
A standard deck of playing cards contains 52 cards. Each card has one of four suits along with a value. The suits
are normally spades, hearts, diamonds and clubs while the values are 2 through 10, Jack, Queen, King and Ace.
Each playing card can be represented using two characters. The first character is the value of the card, with the
values 2 through 9 being represented directly. The characters “T”, “J”, “Q”, “K” and “A” are used to represent the
values 10, Jack, Queen, King and Ace respectively. The second character is used to represent the suit of the card.
It is normally a lowercase letter: “s” for spades, “h” for hearts, “d” for diamonds and “c” for clubs. The following
table provides several examples of cards and their two-character representations.

Begin by writing a function named createDeck. It will use loops to create a complete deck of cards by storing the
two-character abbreviations for all 52 cards into a list. Return the list of cards as the function’s only result. Your
function will not take any parameters.
Write a second function named shuffle that randomizes the order of the cards in a list. One technique that can be
used to shuffle the cards is to visit each element in the list and swap it with another random element in the list.
You must write your own loop for shuffling the cards. You cannot make use of Python’s built-in shuffle function.
Use both of the functions described in the previous paragraphs to create a main program that displays a deck of
cards before and after it has been shuffled. Ensure that your main program only runs when your functions have
not been imported into another file.
"""
import random

def exercise_118():
  before_shuffle = createDeck()
  print(before_shuffle)
  after_shuffle = shuffle(before_shuffle)
  print(after_shuffle)


def createDeck():
  suits = ["S", "D", "C", "H"]
  non_num = {10: "T", 11: "J", 12: "Q", 13: "K", 1: "A"}
  deck = []
  suit = []
  for suit_type in suits:
    for i in range(1, 14):
      if 2 <= i <= 10:
        suit.append(suit_type + str(i))
      else:
        suit.append(suit_type + non_num[i])
    deck.extend(suit)
    suit = []
  return deck

def shuffle(deck):
  final_deck = []
  random_nums = []
  while len(random_nums) < 52:
    random_num = random.randint(0, 51)
    if random_num in random_nums:
      random_num = random.randint(0, 51)
    else:
      random_nums.append(random_num)
  for num in random_nums:
    final_deck.append(deck[num])
  return final_deck
  """
  for num in random_nums:
    new_suit.append(suit[num])
  final_deck.append(new_suit)
  return final_deck
  """


"""
To run code:

from s3_exercises.exec118 import exercise_118 as exec118

exec118()
"""