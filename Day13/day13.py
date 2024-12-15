import re
from math import gcd

# Pattern to extract 2 numbers x and y separated by any 3 characters
pattern = re.compile(r'.*?(\d+).*?(\d+).*?')

# Read input as dict where key = (X, Y) and value = (X, Y), (X, Y)
# Every 3 lines in the input represent a claw machine where line 3 is the prize and lines 1 and 2 are the buttons a, b
with open('input.txt') as f:
    lines = f.readlines()
    claw_machines = {}
    for i in range(0, len(lines), 4):
        a = pattern.match(lines[i]).groups()
        b = pattern.match(lines[i + 1]).groups()
        prize = pattern.match(lines[i + 2]).groups()
        claw_machines[(int(prize[0]), int(prize[1]))] = (int(a[0]), int(a[1])), (int(b[0]), int(b[1]))


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def find_min_presses(prize, button_a, button_b):
    p1, p2 = prize
    a1, a2 = button_a
    b1, b2 = button_b

    # Brute force approach to minimize token cost (3 tokens for button a, 1 token for button b)
    min_tokens = float('inf')
    for x in range(101):  # Limit to at most 100 button presses for a
        for y in range(101):  # Limit to at most 100 button presses for b
            if x * a1 + y * b1 == p1 and x * a2 + y * b2 == p2:
                cost = 3 * x + 1 * y
                min_tokens = min(min_tokens, cost)
    return min_tokens if min_tokens != float('inf') else None


# Part One: Get the fewest number of tokens to win all possible prizes
total_tokens = 0
for prize, (button_a, button_b) in claw_machines.items():
    min_tokens = find_min_presses(prize, button_a, button_b)
    if min_tokens is not None:
        total_tokens += min_tokens
    else:
        continue

print(f"Part One: {total_tokens}")
