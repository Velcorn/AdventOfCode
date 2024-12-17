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
    node, rotations = start
    open_set = {start}
    closed_set = set()
    came_from = {}
    g_score = {node: 0}
    f_score = {node: h(*node, end)}
    direction = 1

    while open_set:
        current, rotations = min(open_set, key=lambda x: f_score[x])
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path, rotations

        open_set.remove(current)
        closed_set.add(current)

        for i, j in directions:
            neighbor = current[0] + i, current[1] + j
            if neighbor in closed_set or maze[neighbor[0]][neighbor[1]] == '#':
                continue

            if (i, j) != directions[direction]:
                rotations += 1000

            tentative_g_score = g_score[current] + 1 + rotations
            if neighbor not in open_set:
                open_set.add((neighbor, rotations))
            elif tentative_g_score >= g_score[neighbor]:
                continue

            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = tentative_g_score + h(*neighbor, end)

    return None


# Part One: Get the lowest score to reach the end
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
start, end = find_char(maze, 'S', first=True), find_char(maze, 'E', first=True)
# Add rotations to start
start = (start, 0)
path, rotations = a_star(maze, start, end)
print(f'Part One: {len(path) + rotations}')
