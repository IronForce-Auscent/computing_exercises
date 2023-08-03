values, suit = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"], ["D", "C", "H", "S"]

def deal():
    return [(values[__import__("random").randint(0, len(values)-1)] + suit[__import__("random").randint(0, len(suit)-1)]) for _ in range(52)]

def points(hand: list[str]):
    total_points, card_count = 0, {card[:-1]: sum(1 for c in hand if c.startswith(card[:-1])) for card in hand}
    total_points += ((card_count.get("J", 0) % 2) + (card_count.get("K", 0) % 2) + (card_count.get("Q", 0) % 2)) * 10
    total_points -= (card_count.get("10", 0) + (card_count.get("J", 0) // 2) + (card_count.get("Q", 0) // 2) + (card_count.get("K", 0) // 2))
    total_points += sum(((lambda a, b: abs(card_count.get(a, 0) - card_count.get(b, 0)) if card_count.get(a, 0) != card_count.get(b, 0) else card_count.get(a, 0))(a, b)) * 5 for a, b in [("A", "9"), ("2", "8"), ("3", "7"), ("4", "6")]) + (card_count.get("5", 0) % 2) * 5  
    return (total_points - (abs(card_count.get("A", 0) - card_count.get("9", 0)) + abs(card_count.get("2", 0) - card_count.get("8", 0)) + abs(card_count.get("3", 0) - card_count.get("7", 0)) + abs(card_count.get("4", 0) - card_count.get("6", 0)) + (card_count.get("5", 0) // 2)))

def main():
    full_deck, midpoint = deal(), 26
    player_1, player_2 = full_deck[:midpoint], full_deck[midpoint:]; p1_points, p2_points = points(player_1), points(player_2)
    print(f"Player 1: {p1_points}\nPlayer 2: {p2_points}\n" + ("Player 1 wins!" if p1_points > p2_points else "Player 2 wins!" if p1_points < p2_points else "Scores are tied"))

main()