# Read input as list of lists for warehouse and single string for moves
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


# Set up for part one and two
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
scaling = {'#': ['#', '#'], '.': ['.', '.'], 'O': ['[', ']'], '@': ['@', '.']}
swarehouse = []
for row in warehouse:
    srow = []
    for cell in row:
        srow.extend(scaling[cell])
    swarehouse.append(srow)


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
    rx, ry = robot
    dx, dy = directions[move]
    nx, ny = rx + dx, ry + dy

    # If next position is free, move the robot
    if warehouse[nx][ny] == '.':
        warehouse[rx][ry] = '.'
        warehouse[nx][ny] = '@'
        robot = (nx, ny)

    # Handle pushing box for standard boxes
    elif warehouse[nx][ny] == 'O':
        new_boxes = []
        while warehouse[nx][ny] == 'O':
            new_boxes.append((nx, ny))
            nx, ny = nx + dx, ny + dy

        if warehouse[nx][ny] == '.':
            rx, ry = new_boxes.pop(0)
            warehouse[robot[0]][robot[1]] = '.'
            warehouse[rx][ry] = '@'
            warehouse[nx][ny] = 'O'
            robot = (rx, ry)

            for box in new_boxes:
                x, y = box
                warehouse[x][y] = 'O'

    # Handle pushing scaled boxes for horizontal moves
    elif warehouse[nx][ny] in ['[', ']'] and move in ['<', '>']:
        new_boxes = []
        while warehouse[nx][ny] in ['[', ']']:
            new_boxes.append((nx, ny))
            nx, ny = nx + dx, ny + dy

        if warehouse[nx][ny] == '.':
            nrx, nry = new_boxes.pop(0)
            warehouse[rx][ry] = '.'
            warehouse[nrx][nry] = '@'
            warehouse[nx][ny] = ']' if move == '>' else '['
            robot = (nrx, nry)

            for i, box in enumerate(new_boxes):
                bx, by = box
                if i % 2 == 0:
                    warehouse[bx][by] = '[' if move == '>' else ']'
                else:
                    warehouse[bx][by] = ']' if move == '>' else '['

    # Handle pushing scaled boxes for vertical moves
    elif warehouse[nx][ny] in ['[', ']'] and move in ['^', 'v']:
        # Helper function to get box sides
        def get_sides(bx, by):
            return (bx, by - 1, bx, by) if warehouse[bx][by] == ']' else (bx, by, bx, by + 1)

        # Helper function to get connected boxes
        def get_boxes(box, move):
            dx, dy = directions[move]
            lbx, lby, rbx, rby = box
            boxes = [(lbx, lby, rbx, rby)]
            visited = set()
            q = [(lbx, lby, rbx, rby)]

            while q:
                lbx, lby, rbx, rby = q.pop(0)
                if (lbx, lby, rbx, rby) in visited:
                    continue

                boxes.append((lbx, lby, rbx, rby))
                visited.add((lbx, lby, rbx, rby))

                lbnx, lbny = lbx + dx, lby + dy
                rbnx, rbny = rbx + dx, rby + dy

                if warehouse[lbnx][lbny] == '#' or warehouse[rbnx][rbny] == '#':
                    return []

                if warehouse[lbnx][lbny] in ['[', ']']:
                    q.append(get_sides(lbnx, lbny))
                if warehouse[rbnx][rbny] in ['[', ']']:
                    q.append(get_sides(rbnx, rbny))

            return boxes

        # Main vertical box pushing logic
        lbx, lby, rbx, rby = get_sides(nx, ny)
        boxes = get_boxes((lbx, lby, rbx, rby), move)

        if boxes:
            for box in reversed(boxes):
                lbx, lby, rbx, rby = box
                lbnx, lbny = lbx + dx, lby + dy
                rbnx, rbny = rbx + dx, rby + dy

                if warehouse[lbnx][lbny] == '.':
                    warehouse[lbx][lby] = '.'
                    warehouse[lbnx][lbny] = '['

                if warehouse[rbnx][rbny] == '.':
                    warehouse[rbx][rby] = '.'
                    warehouse[rbnx][rbny] = ']'

            warehouse[rx][ry] = '.'
            warehouse[nx][ny] = '@'
            robot = (nx, ny)

    return warehouse, robot


# Part One: Get the sum of all boxes' GPS coordinates
robot = find_char(warehouse, '@', first=True)
for move in moves:
    warehouse, robot = move_robot(warehouse, robot, move)
boxes = find_char(warehouse, 'O')
box_coords_sum = sum([100 * x + y for x, y in boxes])
print(f'Part One: {box_coords_sum}')

# Part Two: Get the sum of all boxes' GPS coordinates in scaled warehouse
robot = find_char(swarehouse, '@', first=True)
for move in moves:
    swarehouse, robot = move_robot(swarehouse, robot, move)
boxes = find_char(swarehouse, '[')
box_coords_sum = sum([100 * x + y for x, y in boxes])
print(f'Part Two: {box_coords_sum}')
