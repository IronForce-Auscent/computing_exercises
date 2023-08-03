values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suit = ["D", "C", "H", "S"]

import random
def deal():
    return [(values[random.randint(0, len(values)-1)] + suit[random.randint(0, len(suit)-1)]) for _ in range(52)]

print(deal())