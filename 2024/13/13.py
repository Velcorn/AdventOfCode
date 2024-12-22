import re

# Pattern to extract 2 numbers x and y separated by any 3 characters
pattern = re.compile(r'.*?(\d+).*?(\d+).*?')

# Read input as dict where key = (p1, p2) and value = (a1, a2), (b1, b2)
# Every 3 lines in the input represent a claw machine where line 3 is the prize and lines 1 and 2 are the buttons a, b
with open('input.txt') as f:
    lines = f.readlines()
    claw_machines = []
    for i in range(0, len(lines), 4):
        a = pattern.match(lines[i]).groups()
        b = pattern.match(lines[i + 1]).groups()
        c = pattern.match(lines[i + 2]).groups()
        claw_machines.append([(int(a[0]), int(a[1])), (int(b[0]), int(b[1])), (int(c[0]), int(c[1]))])


# Part One: Get the fewest number of tokens to win all possible prizes
def get_min_tokens(a, b, c):
    # Unpack coordinates
    a1, a2 = a
    b1, b2 = b
    c1, c2 = c

    # Determinant calculation
    det = a1 * b2 - a2 * b1

    # No solution if determinant is zero
    if det == 0:
        return 0

    # Cramer's rule for solving 2x2 system
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det

    # Check if solutions are integers
    if not (x.is_integer() and y.is_integer()):
        return 0

    return int(x * 3 + y)


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
