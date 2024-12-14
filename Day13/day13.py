import re

# Pattern to extract 2 numbers x and y separated by any 3 characters
pattern = re.compile(r'.*?(\d+).*?(\d+).*?')

# Read input as dict where key = (X, Y) and value = (X, Y), (X, Y)
# Every 3 lines in the input represent a claw machine where line 3 is the prize and lines 1 and 2 are the buttons a, b
with open('example.txt') as f:
    lines = f.readlines()
    claw_machines = {}
    for i in range(0, len(lines), 4):
        a = pattern.match(lines[i]).groups()
        b = pattern.match(lines[i + 1]).groups()
        prize = pattern.match(lines[i + 2]).groups()
        claw_machines[(int(prize[0]), int(prize[1]))] = (int(a[0]), int(a[1])), (int(b[0]), int(b[1]))
    print(claw_machines)
