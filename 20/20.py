from collections import deque


def find_char(maze, char):
    for row_idx, row in enumerate(maze):
        if char in row:
            return row_idx, row.index(char)


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def bfs(track, start, end):
    queue = deque([start])
    distances = {start: 0}

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(track)
                and 0 <= ny < len(track[0])
                and track[nx][ny] != '#'
                and (nx, ny) not in distances
            ):
                distances[(nx, ny)] = distances[(x, y)] + 1
                queue.append((nx, ny))

    return distances


def find_cheats(max_cheat_length=2):
    cheats = set()
    for i, ((a, b), d1) in enumerate(distances.items()):
        for (c, d), d2 in list(distances.items())[i:]:
            md = manhattan_distance(a, b, c, d)
            if d2 - d1 - md >= 100 and md <= max_cheat_length:
                cheats.add((a, b, c, d))
    return len(cheats)


# Read the input as a list of lists
with open('20_input.txt') as f:
    track = [list(line.strip()) for line in f]

# Initialize the BFS to find the distances from the start to all other points
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start, end = find_char(track, 'S'), find_char(track, 'E')
distances = bfs(track, start, end)

# Part One: The number of cheats with a length of 2 that save at least 100 picoseconds
cheats = find_cheats(2)
print(f'Part One: {cheats}')

# Part Two: The number of cheats with a max length of 20 that save at least 100 picoseconds
cheats = find_cheats(20)
print(f'Part Two: {cheats}')
