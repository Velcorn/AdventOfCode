import re

# Read input file
with open('input.txt') as f:
    text = f.read()

# Regex pattern to extract do(), don't(), and mul() functions and their arguments
pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))")

# Find all matches
matches = pattern.findall(text)

# Part One: Calculate the sum of pairwise multiplications of numbers
print(f"Part One: {sum(int(item[0]) * int(item[1]) for item in matches if item[0])}")

# Part Two: Calculate the sum of pairwise multiplications of numbers depending on the do and don't functions
do = True
sum = 0
for tpl in matches:
    if tpl[2]:
        do = True
    elif tpl[3]:
        do = False
    elif do:
        sum += int(tpl[0]) * int(tpl[1])

print(f"Part Two: {sum}")
