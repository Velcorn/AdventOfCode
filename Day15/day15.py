# Read input as list of lists and single string of moves
with open('sexample.txt') as f:
    lines = f.read().splitlines()
    warehouse = []
    moves = []
    for line in lines:
        if line.startswith('#'):
            warehouse.append([c for c in line])
        else:
            moves.append(line)
    moves = [c for c in ''.join(moves)]


def find_char(lab, char, first=False):
    if first:
        for row_idx, row in enumerate(lab):
            if char in row:
                return row_idx, row.index(char)
    else:
        indices = set()
        for row_idx, row in enumerate(lab):
            indices.update((row_idx, col_idx) for col_idx, cell in enumerate(row) if cell == char)
        return indices


# Part One: Get the sum of all boxes' GPS coordinates
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
robot = find_char(warehouse, '@', first=True)
for move in moves:
    x, y = robot
    dx, dy = directions[move]
    nx, ny = x + dx, y + dy
    # If next position is free, move the robot
    if warehouse[nx][ny] == '.':
        warehouse[nx][ny] = '@'
        warehouse[x][y] = '.'
        robot = (nx, ny)
    # If next position is a box, check if the box can be pushed, i.e., there is free space anywhere between the box
    # and the wall
    elif warehouse[nx][ny] == 'O':
        if warehouse[nx + dx][ny + dy] == '.':
            warehouse[nx + dx][ny + dy] = 'O'
            warehouse[nx][ny] = '@'
            warehouse[x][y] = '.'
            robot = (nx, ny)
    else:
        continue

for row in warehouse:
    print(''.join(row))

boxes = find_char(warehouse, 'O')
box_coords_sum = sum([100 * x + y for x, y in boxes])
print(f'Part One: {box_coords_sum}')
