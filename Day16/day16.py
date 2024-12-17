# Read input as list of lists for maze
with open('example.txt') as f:
    maze = [list(line.strip()) for line in f]


def find_char(maze, char, first=False):
    if first:
        for row_idx, row in enumerate(maze):
            if char in row:
                return row_idx, row.index(char)
    else:
        indices = set()
        for row_idx, row in enumerate(maze):
            indices.update((row_idx, col_idx) for col_idx, cell in enumerate(row) if cell == char)
        return indices


def h(x, y, end):
    return abs(x - end[0]) + abs(y - end[1])


def a_star(maze, start, end):
    open_set = {start}
    closed_set = set()
    came_from = {}
    g_score = {start: 0}
    f_score = {start: h(*start, end)}
    direction = 1

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path

        open_set.remove(current)
        closed_set.add(current)

        for dx, dy in directions:
            r = 0
            neighbor = nx, ny = current[0] + dx, current[1] + dy
            if neighbor in closed_set or maze[nx][ny] == '#':
                continue

            if neighbor != directions[direction]:
                r = 1

            tentative_g_score = g_score[current] + 1 + r * 1000
            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g_score >= g_score[neighbor]:
                continue

            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = tentative_g_score + h(*neighbor, end)

    return None


# Part One: Get the lowest score to reach the end
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
start, end = find_char(maze, 'S', first=True), find_char(maze, 'E', first=True)
path = a_star(maze, start, end)
d = 1
rotations = 0
node = start
for m in path[1:-1]:
    x, y = node
    nx, ny = m
    d_coords = directions[d]
    nd = directions.index((nx - x, ny - y))
    if nd != d:
        rotations += 1
        d = directions[nd]
    node = m
    if d_coords == 0:
        maze[x][y] = '^'
    elif d_coords == 1:
        maze[x][y] = '>'
    elif d_coords == 2:
        maze[x][y] = 'v'
    elif d_coords == 3:
        maze[x][y] = '<'
for row in maze:
    print(''.join(row))
print(f'Part One: {len(path) + rotations * 1000}')
