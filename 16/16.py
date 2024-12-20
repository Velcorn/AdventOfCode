# Read input as list of lists for maze
with open('input.txt') as f:
    maze = [list(line.strip()) for line in f]


def find_char(maze, char):
    for row_idx, row in enumerate(maze):
        if char in row:
            return row_idx, row.index(char)


def dijkstra(maze, start, end):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    pq = [(0, start[0], start[1], 1, [])]  # (cost, x, y, direction, path_so_far)
    visited = {}
    best_paths = []
    min_total_cost = float('inf')

    while pq:
        # Find the entry with the lowest cost manually
        pq.sort(key=lambda x: x[0])  # Sort by cost
        cost, x, y, current_dir, path = pq.pop(0)  # Pop the first element
        path = path + [(x, y)]

        # Reached the end
        if (x, y) == end:
            total_cost = cost
            if total_cost < min_total_cost:
                best_paths = [path]
                min_total_cost = total_cost
            elif total_cost == min_total_cost:
                best_paths.append(path)
            continue

        # Allow multiple states at same cost
        state = (x, y, current_dir)
        if state in visited and visited[state] < cost:
            continue
        visited[state] = cost

        # Explore all directions
        for new_dir, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#':
                rotation_penalty = 1000 if new_dir != current_dir else 0
                new_cost = cost + 1 + rotation_penalty
                pq.append((new_cost, nx, ny, new_dir, path))

    return best_paths, min_total_cost


# Part One: Get the lowest score to reach the end
start, end = find_char(maze, 'S'), find_char(maze, 'E')
best_paths, total_cost = dijkstra(maze, start, end)
print(f'Part One: {total_cost}')

# Part Two: Get the number of tiles that are part of at least one of the best paths
best_path_tiles = set()
for path in best_paths:
    best_path_tiles.update(path)
print(f'Part Two: {len(best_path_tiles)}')
