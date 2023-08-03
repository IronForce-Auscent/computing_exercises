values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suit = ["D", "C", "H", "S"]

import random
def deal():
    deck = []
    for _ in range(52):
        card_suit, card_value = suit[random.randint(0, len(suit) - 1)], values[random.randint(0, len(values) - 1)]
        deck.append(card_value + card_suit)
    return deck


print(deal())