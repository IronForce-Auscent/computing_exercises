"""
In many card games each player is dealt a specific number of cards after the deck has been shuffled. Write a
function, deal, which takes the number of hands, the number of cards per hand, and a deck of cards as its three
parameters. Your function should return a list containing all of the hands that were dealt. Each hand will be
represented as a list of cards. When dealing the hands, your function should modify the deck of cards passed to
it as a parameter, removing each card from the deck as it is added to a player’s hand. When cards are dealt, it is
customary to give each player a card before any player receives an additional card. Your function should follow
this custom when constructing the hands for the players. Use your solution to Exercise 118 to help you construct
a main program that
creates and shuffles a deck of cards, and then deals out four hands of five cards each. Display all of the hands of
cards, along with the cards remaining in the deck after the hands have been dealt.
"""

def exercise_119():
  player_1 = []
  player_2 = []
  player_3 = []
  player_4 = []
  deck = main()
  for i in range(5):
    random_num = random.randint(0, len(deck))
    player_1.append(deck[random_num])
    del deck[random_num]
    random_num = random.randint(0, len(deck))
    player_2.append(deck[random_num])
    del deck[random_num]
    random_num = random.randint(0, len(deck))
    player_3.append(deck[random_num])
    del deck[random_num]
    random_num = random.randint(0, len(deck))
    player_4.append(deck[random_num])
    del deck[random_num]
  print(f"Player 1 hand: {player_1}")
  print(f"Player 2 hand: {player_2}")
  print(f"Player 3 hand: {player_3}")
  print(f"Player 4 hand: {player_4}")
  print(f"Remaining deck: {deck}")

# Taken from exec118.py
import random

def main():
  return shuffle(createDeck())


def createDeck():
  suits = ["S", "D", "C", "H"]
  non_num = {10: "T", 11: "J", 12: "Q", 13: "K", 1: "A"}
  deck = []
  for suit_type in suits:
    for i in range(1, 14):
      if 2 <= i <= 10:
        deck.append(suit_type + str(i))
      else:
        deck.append(suit_type + non_num[i])
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
To run code:

from s3_exercises.exec119 import exercise_119 as exec119

exec119()
"""