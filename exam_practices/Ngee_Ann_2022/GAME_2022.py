values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suit = ["D", "C", "H", "S"]

import random
def deal():
    deck = []
    for _ in range(52):
        card_suit, card_value = suit[random.randint(0, len(suit) - 1)], values[random.randint(0, len(values) - 1)]
        deck.append(card_value + card_suit)
    return deck

def points(hand: list[str]):
    total_points = 0
    card_count = {"A": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "J": 0, "Q": 0, "K": 0}
    for card in hand:
        card_count[card[:-1]] += 1
        
    total_points += ((card_count["J"] // 2) + (card_count["K"] // 2) + (card_count["Q"] // 2)) * 10
    total_points -= (card_count["10"] + (card_count["J"] // 2) + (card_count["Q"] // 2) + (card_count["K"] // 2))
    # Check for pairs of (1, 9), (2, 8), (3, 7), (4, 6), (5, 5)
    total_points += (card_count["9"] * 5) if card_count["A"] > card_count["9"] else (card_count["9"] * 5) if card_count["A"] < card_count["9"] else (card_count["A"] * 5)
    total_points += (card_count["8"] * 5) if card_count["2"] > card_count["8"] else (card_count["8"] * 5) if card_count["2"] < card_count["8"] else (card_count["2"] * 5)
    total_points += (card_count["7"] * 5) if card_count["3"] > card_count["7"] else (card_count["7"] * 5) if card_count["3"] < card_count["7"] else (card_count["3"] * 5)
    total_points += (card_count["6"] * 5) if card_count["4"] > card_count["6"] else (card_count["6"] * 5) if card_count["4"] < card_count["6"] else (card_count["4"] * 5)
    total_points += (card_count["5"] % 2) * 5
    # Reduce points by the number of non-pairable cards
    total_points -= (abs(card_count["A"] - card_count["9"]) + abs(card_count["2"] - card_count["8"]) + abs(card_count["3"] - card_count["7"]) + abs(card_count["4"] - card_count["6"]) + (card_count["5"] // 2))
    return total_points

def main():
    full_deck = deal()
    midpoint = int(len(full_deck) / 2)
    player_1 = full_deck[:midpoint]
    player_2 = full_deck[midpoint:]
    p1_points, p2_points = points(player_1), points(player_2)
    print(f"Player 1: {p1_points}")
    print(f"Player 2: {p2_points}")
    print("Player 1 wins!" if p1_points > p2_points else "Player 2 wins!" if p1_points < p2_points else "Scores are tied")

main()