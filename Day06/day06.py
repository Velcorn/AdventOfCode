from copy import deepcopy

# Read input file
with open('input.txt') as f:
    lab = [list(line.strip()) for line in f]


# Width, height of the lab and possible directions
width, height = len(lab[0]), len(lab)
directions = [(-1, 0, 'up'), (0, 1, 'right'), (1, 0, 'down'), (0, -1, 'left')]  # Up, Right, Down, Left


def find_char(lab, char):
    for row_idx, row in enumerate(lab):
        if char in row:
            return row_idx, row.index(char)
    return None


def traverse_lab(lab, start):
    # Initialize the current position of the guard
    path = []
    path_set = set()
    visited = set()
    direction = 0
    cur_pos = (start[0], start[1], directions[direction][2])
    while True:
        # Cycle check
        if cur_pos in path_set:
            return path, visited, True
        else:
            path_set.add(cur_pos)

        # Add current position to path and visited set and split into row, col, char for easier handling
        path.append(cur_pos)
        visited.add((cur_pos[0], cur_pos[1]))
        row, col, _ = cur_pos

        # Mark current pos with x
        if lab[row][col] != '^':
            lab[row][col] = 'x'

        # Attempt to move in the current direction
        next_row, next_col = row + directions[direction][0], col + directions[direction][1]

        # Exit condition
        if not (0 <= next_row < height and 0 <= next_col < width):
            break

        # Check boundaries
        if lab[next_row][next_col] in {'#', 'O'}:
            # Turn clockwise if blocked
            direction = (direction + 1) % 4
            next_row, next_col = row + directions[direction][0], col + directions[direction][1]

        # Move to the next position
        cur_pos = (next_row, next_col, directions[direction][2])

    return path, visited, False


# Part One: Number of distinct positions the guard visits in the lab
direction = 0  # Guard starts moving up
start = find_char(lab, '^')
path, visited, _ = traverse_lab(deepcopy(lab), start)

# Print the result
diff_pos_guard = visited
print(f"Part One: {len(diff_pos_guard)}")

# Part Two: Number of distinct positions to place an obstruction
diff_pos_obstructions = set()
for pos in path[1:]:
    # Copy lab for modifications
    lab_copy = deepcopy(lab)

    # Place obstruction at position
    row, col, _ = pos
    lab_copy[row][col] = 'O'

    # Traverse map and add obstruction if loop
    path, visited, loop = traverse_lab(lab_copy, start)
    if loop:
        diff_pos_obstructions.add((pos[0], pos[1]))

print(f'Part Two: {len(diff_pos_obstructions)}')
