from collections import Counter

# Read input file and split into two lists
with open('input.txt') as f:
    llist, rlist = zip(*((int(num1), int(num2)) for num1, num2 in (line.split() for line in f)))

# Part One: Calculate sum of pairwise distances after sorting
print(f"Part One: {sum(abs(x - y) for x, y in zip(sorted(llist), sorted(rlist)))}")

# Part Two: Calculate the sum of left list numbers multiplied by occurrences in the right list
print(f"Part Two: {sum(num * Counter(rlist)[num] for num in llist)}")
