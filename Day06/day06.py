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
    path = [start]
    visited = {start[:2]}
    seen_states = {start}
    cur_pos = start
    while True:
        # Extract row, col and direction from the current position
        row, col, direction = cur_pos

        # Calculate the next position
        x, y = directions[direction]
        next_row, next_col = row + x, col + y

        # While the next position is within the lab and not an obstacle, keep moving
        while 0 <= next_row < height and 0 <= next_col < width and (next_row, next_col) not in obstacles:
            cur_pos = (next_row, next_col, direction)

            # Loop detection
            if cur_pos in seen_states:
                return path, visited, True

            # Update the path, visited set, and seen states
            path.append(cur_pos)
            visited.add((next_row, next_col))
            seen_states.add(cur_pos)

            # Move to the next position
            row, col = next_row, next_col
            next_row, next_col = row + x, col + y

        # If the next position is out of bounds, exit the loop, else change direction
        if not (0 <= next_row < height and 0 <= next_col < width):
            return path, visited, False
        else:
            # Change direction
            cur_pos = (row, col, (direction + 1) % 4)
            path.append(cur_pos)


# General variables
width, height = len(lab[0]), len(lab)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
char_idx = find_char(lab, '^', first=True)
obstacles = find_char(lab, '#', first=False)

# Part One: Number of distinct positions the guard visits in the lab
start = (char_idx[0], char_idx[1], 0)  # Row, Col, Direction
path, visited, _ = traverse_lab(start, obstacles)
diff_pos_guard = visited
print(f"Part One: {len(diff_pos_guard)}")

# Part Two: Number of distinct positions to place an obstruction
diff_pos_obstructions = set()
visited.remove((start[0], start[1]))
for row, col in visited:
    # Place an obstruction at the current position
    obstruction = (row, col)

    # Traverse the lab from the position before the new obstruction
    path, _, loop = traverse_lab(path[0], obstacles | {obstruction})
    if loop:
        diff_pos_obstructions.add(obstruction)

print(f'Part Two: {len(diff_pos_obstructions)}')
