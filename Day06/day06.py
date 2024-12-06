import numpy as np

# Read input file
with open('input.txt') as f:
    map_ = [[char for char in line.strip()] for line in f]

# Part One: Number of distinct positions the guard visits on the map
width, height = len(map_[0]), len(map_)
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
direction = 0
char = '^'
current_position = (0, 0)
for row in map_:
    if char in row:
        current_position = (map_.index(row), row.index(char))
visited = {current_position}
distinct_positions = 1
next_position = (current_position[0] + directions[direction][0], current_position[1] + directions[direction][1])
while 0 <= next_position[0] < width and 0 <= next_position[1] < height:
    map_[current_position[0]][current_position[1]] = 'X'
    if map_[next_position[0]][next_position[1]] != '#':
        current_position = next_position
        if next_position not in visited:
            visited.add(next_position)
            distinct_positions += 1
    else:
        direction = direction + 1 if direction < 3 else 0
    next_position = (current_position[0] + directions[direction][0], current_position[1] + directions[direction][1])

for row in map_:
    print(row)

print(f"Part One: {distinct_positions}")
