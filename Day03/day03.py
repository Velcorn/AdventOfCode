import re

# Read input file
with open('input.txt') as f:
    text = f.read()

# Regex pattern to extract do(), don't(), and mul() functions and their arguments
pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))")

# Part One: Calculate the sum of pairwise multiplications of numbers
print(f"Part One: {sum(int(item[0]) * int(item[1]) for item in pattern.findall(text) if item[0])}")

# Part Two: Calculate the sum of pairwise multiplications of numbers depending on the do and don't functions
items = pattern.findall(text)
do = True
total = 0
for item in items:
    if item[2]:
        do = True
    elif item[3]:
        do = False
    elif do:
        total += int(item[0]) * int(item[1])

print(f"Part Two: {total}")
