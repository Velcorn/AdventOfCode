import re
from math import log2

pattern = re.compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)')

# Read input as list of tuples (p1, p2, v1, v2)
file = 'input.txt'
with open(file) as f:
    lines = f.readlines()
    robots = {}
    for i, line in enumerate(lines):
        p1, p2, v1, v2 = pattern.match(line).groups()
        robots[i] = (int(p1), int(p2), int(v1), int(v2))

# Part One: Calculate the safety factor after 100 seconds
# The safety factor is the number of robots within each quadrant of the grid multiplied by each other
w, h = (11, 7) if file == 'example.txt' else (101, 103)
grid = [[0 for x in range(w)] for y in range(h)]
for i in range(len(robots)):
    x, y, vx, vy = robots.get(i)
    nx, ny = (x + 100 * vx) % w, (y + vy * 100) % h
    grid[ny][nx] += 1
q1 = sum(grid[y][x] for y in range(h // 2) for x in range(w // 2))
q2 = sum(grid[y][x] for y in range(h // 2) for x in range(w // 2 + 1, w))
q3 = sum(grid[y][x] for y in range(h // 2 + 1, h) for x in range(w // 2))
q4 = sum(grid[y][x] for y in range(h // 2 + 1, h) for x in range(w // 2 + 1, w))
print(f'Part One: {q1 * q2 * q3 * q4}')


# Part Two: Get the fewest number of seconds that must elapse for the robots to display a christmas tree
def calculate_entropy(grid):
    w, h = len(grid[0]), len(grid)
    total_pixels = w * h

    # Calculate the entropy of the grid
    ones = sum(1 if grid[y][x] > 0 else 0 for y in range(h) for x in range(w))
    zeros = total_pixels - ones

    p_ones = ones / total_pixels
    p_zeros = zeros / total_pixels

    entropy = 0
    if 0 < p_ones < 1:
        entropy = -(p_zeros * log2(p_zeros) + p_ones * log2(p_ones))

    return entropy


grid = [[0 for x in range(w)] for y in range(h)]
safety_factor = 0
seconds = 0
while True:
    for i in range(len(robots)):
        x, y, vx, vy = robots.get(i)
        nx, ny = (x + vx) % w, (y + vy) % h
        robots[i] = (nx, ny, vx, vy)
        grid[ny][nx] += 1
        if grid[y][x] > 0:
            grid[y][x] -= 1
    seconds += 1
    entropy = calculate_entropy(grid)
    if entropy < 0.27:
        with open(f'grid_{seconds}.txt', 'w') as f:
            for row in grid:
                f.write(''.join(str(x) for x in row) + '\n')
print(f'Part Two: {seconds}')
