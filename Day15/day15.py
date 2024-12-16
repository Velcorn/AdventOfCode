from copy import deepcopy
from time import sleep

# Read input as list of lists and single string of moves
with open('lexample.txt') as f:
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


def smove_robot(swarehouse, robot, move):
    x, y = robot
    dx, dy = directions[move]
    nx, ny = x + dx, y + dy
    # If next position is free, move the robot
    if swarehouse[nx][ny] == '.':
        swarehouse[x][y] = '.'
        swarehouse[nx][ny] = '@'
        robot = (nx, ny)
    # If next position is a box, check if the box can be pushed, i.e., there is free space anywhere between the box
    # and the wall and push the box and adjacent boxes if any
    elif swarehouse[nx][ny] in ['[', ']'] and move in ['<', '>']:
        new_boxes = []
        while swarehouse[nx][ny] in ['[', ']']:
            new_boxes.append((nx, ny))
            nx, ny = nx + dx, ny + dy
        if swarehouse[nx][ny] == '.':
            rx, ry = new_boxes.pop(0)
            swarehouse[x][y] = '.'
            swarehouse[rx][ry] = '@'
            swarehouse[nx][ny] = ']' if move == '>' else '['
            robot = (rx, ry)
            for i, box in enumerate(new_boxes):
                x, y = box
                if i % 2 == 0:
                    swarehouse[x][y] = '[' if move == '>' else ']'
                else:
                    swarehouse[x][y] = ']' if move == '>' else '['
    elif swarehouse[nx][ny] in ['[', ']'] and move in ['^', 'v']:
        new_boxes = []
        bside = swarehouse[nx][ny]
        # With each step, look at the
        while swarehouse[nx][ny] in ['[', ']']:
            new_boxes.append((nx, ny, swarehouse[nx][ny]))
            nx, ny = nx + dx, ny + dy
        if swarehouse[nx][ny] == '.':
            rx, ry, bside = new_boxes.pop(0)
            swarehouse[x][y] = '.'
            swarehouse[rx][ry] = '@'
            swarehouse[nx][ny] = bside
            robot = (rx, ry)
            for i, box in enumerate(new_boxes):
                x, y = box
                if i % 2 == 0:
                    swarehouse[x][y] = '[' if move == 'v' else ']'
                else:
                    swarehouse[x][y] = ']' if move == 'v' else '['
    return swarehouse, robot


# Part One: Get the sum of all boxes' GPS coordinates
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
robot = find_char(warehouse, '@', first=True)
warehouse_ = deepcopy(warehouse)
for move in moves:
    warehouse_, robot = move_robot(warehouse_, robot, move)
boxes = find_char(warehouse_, 'O')
box_coords_sum = sum([100 * x + y for x, y in boxes])
print(f'Part One: {box_coords_sum}')

# Part Two: Get the sum of all boxes' GPS coordinates in scaled warehouse
scaling = {'#': ['#', '#'], '.': ['.', '.'], 'O': ['[', ']'], '@': ['@', '.']}
swarehouse = []
for row in warehouse:
    srow = []
    for cell in row:
        srow.extend(scaling[cell])
    swarehouse.append(srow)
for row in swarehouse:
    print(''.join(row))
print()
robot = find_char(swarehouse, '@', first=True)
swarehouse_ = deepcopy(swarehouse)
for move in moves:
    swarehouse_, robot = smove_robot(swarehouse_, robot, move)
    for row in swarehouse_:
        print(''.join(row))
    print(move)
    sleep(1)
