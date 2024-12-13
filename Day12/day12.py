# Read input as list of lists
with open('example.txt') as f:
    garden_plots = [[char for char in line.strip()] for line in f]


# For each plant (A-Z), perform a BFS only moving to same type of plant while tracking the perimeter, i.e.,
# adjacent plants of a different type or out of bounds. The result is the area of the garden plot, i.e., the
# number of plants visited multiplied by the perimeter.
def get_fencing_prices(garden_plots, discount):
    visited_plots = set()

    def bfs(visited, i, j, discount):
        if (i, j) in visited_plots:
            return 0
        else:
            visited.add((i, j))
        visited_plants = set()
        plant_type = garden_plots[i][j]
        perimeter = 0
        unique_boundaries = set()
        q = [(i, j)]
        while q:
            i, j = q.pop(0)
            if (i, j) in visited_plants:
                continue
            visited_plots.add((i, j))
            visited_plants.add((i, j))
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for x, y in neighbors:
                if 0 <= x < len(garden_plots) and 0 <= y < len(garden_plots[0]):
                    if garden_plots[x][y] == plant_type:
                        q.append((x, y))
                    else:
                        perimeter += 1
                else:
                    perimeter += 1
        area = len(visited_plants)
        sides = len(unique_boundaries)
        if discount:
            return area * sides
        return area * perimeter
    return sum(bfs(visited_plots, i, j, discount) for i in range(len(garden_plots)) for j in range(len(garden_plots[0])))


# Part One: Get the total price of fencing for the garden plots
for row in garden_plots:
    print(row)
print(f'Part One: {get_fencing_prices(garden_plots, discount=False)}')

# Part Two: Get the total price of fencing for the garden plots with a discount
print(f'Part Two: {get_fencing_prices(garden_plots, discount=True)}')
