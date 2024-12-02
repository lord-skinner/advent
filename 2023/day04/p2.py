card_map = {}
for card_num, card_info in enumerate(open("day04.txt", "r")):
    if card_num not in card_map:
        card_map[card_num] = 1

    cards = card_info.split(": ")[1].split(" | ")
    input1 = list(map(int, cards[0].split()))
    input2 = list(map(int, cards[-1].split()))
    matching_numbers = sum(numb in input1 for numb in input2)
    if matching_numbers != 0:
        for _ in range(card_num + 1, card_num + matching_numbers + 1):
            card_map[_] = card_map.get(_, 1) + card_map[card_num]
print(sum(card_map.values()))