import re

pattern = re.compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)')

# Read input as list of tuples (p1, p2, v1, v2)
with open('example.txt') as f:
    lines = f.readlines()
    robots = []
    for line in lines:
        p1, p2, v1, v2 = pattern.match(line).groups()
        robots.append((int(p1), int(p2), int(v1), int(v2)))


# Part One: Calculate the safety factor after 100 seconds
# The safety factor is the number of robots within each quadrant of the grid multiplied by each other
w, h = 11, 7
grid = [[0 for x in range(w)] for y in range(h)]

