from collections import Counter
from functools import cmp_to_key

def hand_type(hand):
    counts = sorted(Counter(hand).values(), reverse=True)
    if counts[0] == 5:
        return 7  # Five of a kind
    elif counts[0] == 4:
        return 6  # Four of a kind
    elif counts[0] == 3 and counts[1] == 2:
        return 5  # Full house
    elif counts[0] == 3:
        return 4  # Three of a kind
    elif counts[0] == 2 and counts[1] == 2:
        return 3  # Two pair
    elif counts[0] == 2:
        return 2  # One pair
    else:
        return 1  # High card

def compare_hands(hand1, hand2):
    type1 = hand_type(hand1[0])
    type2 = hand_type(hand2[0])
    if type1 != type2:
        return type1 - type2
    
    card_order = "AKQJT98765432"
    for c1, c2 in zip(hand1[0], hand2[0]):
        if c1 != c2:
            return card_order.index(c2) - card_order.index(c1)
    return 0

# Read input
hands = []
with open('input.txt', 'r') as file:
    for line in file:
        hand, bid = line.strip().split()
        hands.append((hand, int(bid)))

# Sort hands
sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

# Calculate total winnings
total_winnings = sum(rank * hand[1] for rank, hand in enumerate(sorted_hands, 1))

print(f"Total winnings: {total_winnings}")