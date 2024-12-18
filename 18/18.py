# Read input as list of tuples with integer coordinates
with open('18_example.txt') as f:
    corruptions = [tuple(map(int, line.strip().split(','))) for line in f]


def bfs(memory_space, start, goal):
    queue = [(start, 0)]
    visited = {start}
    while queue:
        (x, y), steps = queue.pop(0)
        if (x, y) == goal:
            return steps
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= nx < size and 0 <= ny < size and memory_space[nx][ny] != '#' and (nx, ny) not in visited:
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))
    return -1


# Part One: Get the minimum number of steps to reach the exit
size, sims = (7, 12) if 'example' in f.name else (71, 1024)
memory_space = [['.' for _ in range(size)] for _ in range(size)]
for x, y in corruptions[:sims]:
    memory_space[y][x] = '#'
start, goal = (0, 0), (size - 1, size - 1)
print(f'Part One: {bfs(memory_space, start, goal)}')

# Part Two: Get the first coordinate that blocks the path to the exit
for x, y in corruptions[sims:]:
    memory_space[y][x] = '#'
    steps = bfs(memory_space, start, goal)
    if steps == -1:
        print(f'Part Two: {x},{y}')
        break
