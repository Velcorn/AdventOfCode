from copy import deepcopy

# Read input file and split it into a list of lists
with open('input.txt') as f:
    lab = [list(line.strip()) for line in f]


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


def traverse_lab(start, obstacles):
    path = []
    visited = set()
    seen_states = set()
    cur_pos = start
    while True:
        # Extract row, col and direction from the current position
        row, col, direction = cur_pos

        # Attempt to move in the current direction
        for _ in range(4):
            x, y = directions[direction]
            next_row, next_col = row + x, col + y

            # Check boundaries, obstacles/obstructions and seen states
            if not (0 <= next_row < height and 0 <= next_col < width):
                path.append(cur_pos)
                visited.add((row, col))
                return path, visited, False
            elif (next_row, next_col) in obstacles:
                direction = (direction + 1) % 4
            elif (next_row, next_col, direction) in seen_states:
                return path, visited, True
            else:
                # Add current position to path and seen states, and mark coordinates as visited
                path.append(cur_pos)
                seen_states.add(cur_pos)
                visited.add((row, col))

                # Move to the next position
                cur_pos = (next_row, next_col, direction)
                break


# General variables
width, height = len(lab[0]), len(lab)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
char_idx = find_char(lab, '^', first=True)
start = (char_idx[0], char_idx[1], 0)  # Row, Col, Direction
obstacles = find_char(lab, '#', first=False)

# Part One: Number of distinct positions the guard visits in the lab
path, visited, _ = traverse_lab(start, obstacles)
diff_pos_guard = visited
print(f"Part One: {len(diff_pos_guard)}")

# Part Two: Number of distinct positions to place an obstruction
diff_pos_obstructions = set()
for row, col in visited:
    obstruction = (row, col)

    # Traverse the lab from the original starting point with the obstruction
    _, _, loop = traverse_lab(start, obstacles | {obstruction})
    if loop:
        diff_pos_obstructions.add(obstruction)

print(f'Part Two: {len(diff_pos_obstructions)}')
