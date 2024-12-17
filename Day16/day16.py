# Read input as list of lists for maze
with open('example.txt') as f:
    maze = [list(line.strip()) for line in f]


def find_char(maze, char, first=False):
    if first:
        for row_idx, row in enumerate(maze):
            if char in row:
                return row_idx, row.index(char)


def h(x, y, end):
    """ Heuristic function: Manhattan distance """
    return abs(x - end[0]) + abs(y - end[1])


def a_star(maze, start, end):
    """ A* search algorithm tracking rotations only """
    open_set = {start}
    closed_set = set()
    came_from = {}
    f_score = {start: h(*start, end)}
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    direction_index = 0  # Initial direction (Up)
    rotations = 0  # Rotation counter

    while open_set:
        # Pick the node with the lowest f_score
        current = min(open_set, key=lambda x: f_score[x])

        # Reached the end
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path, rotations

        open_set.remove(current)
        closed_set.add(current)

        # Explore neighbors
        for i, (dx, dy) in enumerate(directions):
            neighbor = nx, ny = current[0] + dx, current[1] + dy

            # Ignore walls or already-visited cells
            if not (0 <= nx < len(maze) and 0 <= ny < len(maze[0])) or maze[nx][ny] == '#' or neighbor in closed_set:
                continue

            # Count rotation if direction changes
            rotation_penalty = 1 if i != direction_index else 0

            # Update rotations and path
            if neighbor not in open_set or rotation_penalty == 1:
                came_from[neighbor] = current
                f_score[neighbor] = h(*neighbor, end)
                open_set.add(neighbor)
                if rotation_penalty:
                    rotations += 1
                direction_index = i

    return None, None


# Part One: Find the path and count rotations
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
start = find_char(maze, 'S', first=True)
end = find_char(maze, 'E', first=True)
path, rotations = a_star(maze, start, end)

# Mark the path on the maze
for x, y in path:
    if maze[x][y] not in ['S', 'E']:
        maze[x][y] = '+'
for row in maze:
    print(''.join(row))
    
print(f'Part One: {len(path) + rotations * 1000}')    