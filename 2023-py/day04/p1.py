ans1 = 0
for card_num, card_info in enumerate(open("day04.txt", "r")):
    cards = card_info.split(": ")[1].split(" | ")
    input1 = set(map(int, cards[0].split()))
    input2 = set(map(int, cards[-1].split()))
    matching_numbers = len(input1.intersection(input2))
    if matching_numbers != 0:
        x , y = 1, matching_numbers
        for _ in range(y - 1):
            x *= 2
        ans1 += x
print(ans1)