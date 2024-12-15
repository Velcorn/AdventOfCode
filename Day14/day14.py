import re

pattern = re.compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)')

# Read input as list of tuples (p1, p2, v1, v2)
file = 'input.txt'
with open(file) as f:
    lines = f.readlines()
    robots = {}
    for i, line in enumerate(lines):
        p1, p2, v1, v2 = pattern.match(line).groups()
        robots[i] = (int(p1), int(p2), int(v1), int(v2))

# Initialize grid with dimensions w x h
w, h = (11, 7) if file == 'example.txt' else (101, 103)
grid = [[0 for x in range(w)] for y in range(h)]

# Part One: Calculate the safety factor after 100 seconds
# The safety factor is the number of robots within each quadrant of the grid multiplied by each other
grid_ = grid.copy()
for i in range(len(robots)):
    x, y, vx, vy = robots[i]
    nx, ny = (x + 100 * vx) % w, (y + vy * 100) % h
    grid_[ny][nx] += 1
q1 = sum(grid_[y][x] for y in range(h // 2) for x in range(w // 2))
q2 = sum(grid_[y][x] for y in range(h // 2) for x in range(w // 2 + 1, w))
q3 = sum(grid_[y][x] for y in range(h // 2 + 1, h) for x in range(w // 2))
q4 = sum(grid_[y][x] for y in range(h // 2 + 1, h) for x in range(w // 2 + 1, w))
safety_factor = q1 * q2 * q3 * q4
print(f'Part One: {safety_factor}')


# Part Two: Get the fewest number of seconds that must elapse for the robots to display a christmas tree
grid_ = grid.copy()
seconds = 0
while True:
    for i in range(len(robots)):
        x, y, vx, vy = robots[i]
        nx, ny = (x + vx) % w, (y + vy) % h
        robots[i] = (nx, ny, vx, vy)
        grid_[ny][nx] += 1
        if grid_[y][x] > 0:
            grid_[y][x] -= 1
    seconds += 1
    row = ''.join(['#' if grid_[y][x] > 0 else '.' for x in range(w) for y in range(h)])
    # ####### best tree detector: can't be bothered to implement a proper one
    if '########' in row:
        with open('output.txt', 'w') as f:
            f.write('\n'.join([''.join(['#' if grid_[y][x] > 0 else '.' for x in range(w)]) for y in range(h)]))
        break
print(f'Part Two: {seconds}')
