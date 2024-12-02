import re
numbers = 'one two three four five six seven eight nine'.split()
regex = "(?=(" + "|".join(numbers) + "|\\d))"
number_map = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

def word_to_number(word):
    return number_map.get(word, word)

ans2 = 0
for line in open("day01.txt", "r"):
    matches = re.findall(regex, line)
    converted = [word_to_number(match) for match in matches]
    ans2 += int(converted[0] + converted[-1])
print(ans2)