import re

# Regex pattern to extract do(), don't(), and mul() functions and their arguments
pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))")

# Read input file and find all matches
with open('input.txt') as f:
    matches = pattern.findall(f.read())

# Part One: Calculate the sum of pairwise multiplications of numbers
mul_sum = sum(int(item[0]) * int(item[1]) for item in matches if item[0])
print(f"Part One: {mul_sum}")

# Part Two: Calculate the sum of pairwise multiplications of numbers, where do enables and don't disables
do = True
mul_sum_do_dont = 0
for tpl in matches:
    if tpl[2]:
        do = True
    elif tpl[3]:
        do = False
    elif do:
        mul_sum_do_dont += int(tpl[0]) * int(tpl[1])

print(f"Part Two: {mul_sum_do_dont}")
