# Read input as list of lists
with open('example.txt') as f:
    plots = [[char for char in line.strip()] for line in f]


# For each plant (A-Z), perform a BFS only moving to same type of plant while tracking the perimeter, i.e.,
# adjacent plants of a different type or out of bounds. The result is the area of the garden plot, i.e., the
# number of plants visited multiplied by the perimeter or sides of the garden plot if discounted.
def get_fencing_prices(plots, discount):
    visited_plots = set()

    def unique_boundary(node, neighbor):
        # Add unique boundary, i.e., relevant coordinate of current node (either (0, j) or (i, 0))
        # and direction of boundary (N, S, W, E)
        i, j = node
        x, y = neighbor
        if x < i:
            return i, 0, 'N'
        elif x > i:
            return i, 0, 'S'
        elif y < j:
            return 0, j, 'W'
        else:
            return 0, j, 'E'

    def bfs(visited, i, j, discount):
        if (i, j) in visited_plots:
            return 0
        else:
            visited.add((i, j))
        plant_type = plots[i][j]
        visited_plants = set()
        perimeter = 0
        unique_boundaries = set()
        q = [(i, j)]
        while q:
            i, j = q.pop(0)
            if (i, j) in visited_plants:
                continue
            visited_plots.add((i, j))
            visited_plants.add((i, j))
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for x, y in neighbors:
                if 0 <= x < len(plots) and 0 <= y < len(plots[0]):
                    if plots[x][y] == plant_type:
                        q.append((x, y))
                    else:
                        perimeter += 1
                        unique_boundaries.add(unique_boundary((i, j), (x, y)))
                else:
                    perimeter += 1
                    unique_boundaries.add(unique_boundary((i, j), (x, y)))
        area = len(visited_plants)
        if discount:
            sides = len(unique_boundaries)
            print(f'Plant: {plant_type}, Area: {area}, Sides: {sides}')
            return area * sides
        return area * perimeter
    return sum(bfs(visited_plots, i, j, discount) for i in range(len(plots)) for j in range(len(plots[0])))


# Part One: Get the total price of fencing for the garden plots
for row in plots:
    print(''.join(row))

print(f'Part One: {get_fencing_prices(plots, discount=False)}')

# Part Two: Get the total price of fencing for the garden plots with a discount
print(f'Part Two: {get_fencing_prices(plots, discount=True)}')
