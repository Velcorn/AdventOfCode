# Read input as list of lists and single string of moves
with open('input.txt') as f:
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


def move_robot(warehouse, robot, move):
    x, y = robot
    dx, dy = directions[move]
    nx, ny = x + dx, y + dy
    # If next position is free, move the robot
    if warehouse[nx][ny] == '.':
        warehouse[x][y] = '.'
        warehouse[nx][ny] = '@'
        robot = (nx, ny)
    # If next position is a box, check if the box can be pushed, i.e., there is free space anywhere between the box
    # and the wall and push the box and adjacent boxes if any
    elif warehouse[nx][ny] == 'O':
        new_boxes = []
        while warehouse[nx][ny] == 'O':
            new_boxes.append((nx, ny))
            nx, ny = nx + dx, ny + dy
        if warehouse[nx][ny] == '.':
            rx, ry = new_boxes.pop(0)
            warehouse[x][y] = '.'
            warehouse[rx][ry] = '@'
            warehouse[nx][ny] = 'O'
            robot = (rx, ry)
            for box in new_boxes:
                x, y = box
                warehouse[x][y] = 'O'
    return warehouse, robot


# Part One: Get the sum of all boxes' GPS coordinates
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
robot = find_char(warehouse, '@', first=True)
for move in moves:
    warehouse, robot = move_robot(warehouse, robot, move)
    for row in warehouse:
        print(''.join(row))
    print()


boxes = find_char(warehouse, 'O')
box_coords_sum = sum([100 * x + y for x, y in boxes])
print(f'Part One: {box_coords_sum}')
