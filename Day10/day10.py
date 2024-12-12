# Read input as list of lists
with open('example.txt') as f:
    top_map = [[int(char) for char in line.strip()] for line in f]


# Find all trailheads in the topographical map
def find_trailheads(top_map):
    trailheads = []
    for i, row in enumerate(top_map):
        for j, val in enumerate(row):
            if val == 0:
                trailheads.append((i, j))
    return trailheads


# Find all distinct 9-height positions that can be reached from a trailhead and all possible paths to reach them
def find_paths(top_map, trailhead):
    paths = []
    seen_nines = set()
    queue = [(trailhead, [trailhead])]
    while queue:
        (i, j), path = queue.pop(0)
        val = top_map[i][j]
        if val == 9:
            paths.append(path)
            seen_nines.add((i, j))
            continue
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < len(top_map) and 0 <= y < len(top_map[0]):
                if top_map[x][y] == val + 1:
                    queue.append(((x, y), path + [(x, y)]))
    return len(paths), len(seen_nines)


# Part One: Get the sum of the scores of all trailheads - number of distinct 9-height positions that can be reached
# Part Two: Get the sum of the ratings of all trailheads - number of possible paths to reach 9-height positions
trailheads = find_trailheads(top_map)
sum_scores = 0
sum_ratings = 0
for trailhead in trailheads:
    paths, score = find_paths(top_map, trailhead)
    sum_scores += score
    sum_ratings += paths
print(f'Part One: {sum_scores}')
print(f'Part Two: {sum_ratings}')
