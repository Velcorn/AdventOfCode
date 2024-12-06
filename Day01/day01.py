from collections import Counter

# Read input file and split into two lists
with open('input.txt') as f:
    llist, rlist = zip(*((int(num1), int(num2)) for num1, num2 in (line.split() for line in f)))

# Part One: Calculate sum of pairwise distances after sorting
total_distance = sum(abs(x - y) for x, y in zip(sorted(llist), sorted(rlist)))
print(f"Part One: {total_distance}")

# Part Two: Calculate the sum of left list numbers multiplied by occurrences in the right list
similarity_score = sum(num * Counter(rlist)[num] for num in llist)
print(f"Part Two: {similarity_score}")
