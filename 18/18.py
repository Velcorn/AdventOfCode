from heapq import heappush, heappop


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path


def a_star(memory_space, start, goal):
    frontier = [(0, start)]  # priority queue with (f_score, position)
    came_from = {}
    g_score = {start: 0}
    f_score = {start: manhattan_distance(start, goal)}

    while frontier:
        _, current = heappop(frontier)

        if current == goal:
            return g_score[current], get_path(came_from, current)

        for nx, ny in [(current[0] - 1, current[1]), (current[0] + 1, current[1]),
                       (current[0], current[1] - 1), (current[0], current[1] + 1)]:
            if 0 <= nx < len(memory_space) and 0 <= ny < len(memory_space[0]) and memory_space[nx][ny] != '#':
                neighbor = (nx, ny)
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + manhattan_distance(neighbor, goal)
                    heappush(frontier, (f_score[neighbor], neighbor))

    return -1, []


# Read input as list of lists
with open('18_input.txt') as f:
    corruptions = [tuple(map(int, line.strip().split(','))) for line in f]

# Initialize parameters
size, sims = (7, 12) if 'example' in f.name else (71, 1024)
memory_space = [['.' for _ in range(size)] for _ in range(size)]
start, goal = (0, 0), (size - 1, size - 1)

# Part One: Get the minimum number of steps to reach the exit
for y, x in corruptions[:sims]:
    memory_space[x][y] = '#'
steps, best_path = a_star(memory_space, start, goal)
print(f'Part One: {steps}')

# Part Two: Find first corruption that blocks the path
best_path_set = set(best_path)
for x, y in corruptions[sims:]:
    if (x, y) in best_path_set:
        memory_space[y][x] = '#'
        steps, new_path = a_star(memory_space, start, goal)
        if steps == -1:
            print(f'Part Two: {x},{y}')
            break
        current_path = new_path
    else:
        memory_space[y][x] = '#'
        # Only run A* if corruption is adjacent to current path
        if any((y+dy, x+dx) in best_path for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]):
            steps, new_path = a_star(memory_space, start, goal)
            if steps == -1:
                print(f'Part Two: {x},{y}')
                break
            best_path = new_path
