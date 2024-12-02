ans1 = 0
for line in open("day01.txt", "r"):
  numbers = [char for char in line if char.isdigit()]
  ans1 += int(numbers[0]+numbers[-1])
print(ans1)