import re
from math import gcd, floor, ceil

# Pattern to extract 2 numbers x and y separated by any 3 characters
pattern = re.compile(r'.*?(\d+).*?(\d+).*?')

# Read input as dict where key = (p1, p2) and value = (a1, a2), (b1, b2)
# Every 3 lines in the input represent a claw machine where line 3 is the prize and lines 1 and 2 are the buttons a, b
with open('example.txt') as f:
    lines = f.readlines()
    claw_machines = []
    for i in range(0, len(lines), 4):
        a = pattern.match(lines[i]).groups()
        b = pattern.match(lines[i + 1]).groups()
        c = pattern.match(lines[i + 2]).groups()
        claw_machines.append([(int(a[0]), int(a[1])), (int(b[0]), int(b[1])), (int(c[0]), int(c[1]))])


# Part One: Get the fewest number of tokens to win all possible prizes
# Two diophantine equations are formed for each claw machine, only one of which is needed to solve the problem
def extended_euclidean(a, b):
    if b == 0:
        return 1, 0
    x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return x, y


def get_min_tokens(a, b, c):
    # Extract individual values
    a1, a2 = a
    b1, b2 = b
    c1, c2 = c

    # Return 0 if no integer solution exists
    g1, g2 = gcd(a1, b1), gcd(a2, b2)
    if c1 % g1 != 0 or c2 % g2 != 0:
        return 0

    # Use extended Euclidean algorithm
    x0, y0 = extended_euclidean(a1, b1)

    x, y = x0 + b1 // g1, y0 - a1 // g1

    return x * 3 + y


# Part One: Get the fewest tokens to win all possible prizes
fewest_tokens = 0
for a, b, c in claw_machines:
    fewest_tokens += get_min_tokens(a, b, c)
print(f'Part One: {fewest_tokens}')


# Part Two: Part One with updated price positions
offset = 10000000000000
fewest_tokens = 0
for a, b, c in claw_machines:
    c = c[0] + offset, c[1] + offset
    fewest_tokens += get_min_tokens(a, b, c)
print(f'Part Two: {fewest_tokens}')
