from heapq import heappop, heappush

# Read the input as list of lists
with open('20_input.txt') as f:
    track = [list(line.strip()) for line in f]


def find_char(maze, char):
    for row_idx, row in enumerate(maze):
        if char in row:
            return row_idx, row.index(char)


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(track, start, end, threshold=None):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    open_set = [(0, start[0], start[1], [])]  # (estimated_cost, x, y, path_so_far)
    g_costs = {start: 0}  # Cost to reach each node
    visited = set()

    while open_set:
        # Pop the node with the lowest estimated cost
        est_cost, x, y, path = heappop(open_set)
        path = path + [(x, y)]

        # Reached the end
        if (x, y) == end:
            return path

        # If cost is geq threshold, return
        if threshold is not None and len(path) - 1 >= threshold:
            return []

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(track) and 0 <= ny < len(track[0]) and track[nx][ny] != '#':
                tentative_g_cost = g_costs[(x, y)] + 1
                neighbor = (nx, ny)

                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + manhattan_distance(neighbor, end)
                    heappush(open_set, (f_cost, nx, ny, path))

    return []


# Part One: The number of cheats that save at least 100 picoseconds
start, end = find_char(track, 'S'), find_char(track, 'E')
path = a_star(track, start, end)
threshold = len(path) - 101
# Walk over the path and add neighboring walls to the list if they have the path on the other side
walls = set()
for x, y in path:
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(track) - 1 and 0 <= ny < len(track[0]) - 1 and track[nx][ny] == '#':
            nnx, nny = nx + dx, ny + dy
            if (nnx, nny) in path:
                walls.add((nx, ny))


def test_wall_batch(track, walls, start, end, threshold):
    """Temporarily remove walls and run A*."""
    for x, y in walls:
        track[x][y] = '.'
    path = a_star(track, start, end)
    for x, y in walls:
        track[x][y] = '#'
    return path if path and len(path) - 1 < threshold else None


cheated = []
i = 0
for x, y in walls:
    if i % 100 == 0:
        print(f'{i}/{len(walls)}')
    track[x][y] = '.'
    path = a_star(track, start, end, threshold)
    if path:
        cheated.append((x, y))
    track[x][y] = '#'
    i += 1
print(f'Part One: {len(cheated)}')
