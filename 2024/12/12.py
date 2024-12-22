# Read input as list of lists
with open('input.txt') as f:
    garden = [[char for char in line.strip()] for line in f]


# Zero-padding the plots to avoid out of bounds errors
garden = [['0'] + row + ['0'] for row in garden]
garden = [['0'] * len(garden[0])] + garden + [['0'] * len(garden[0])]


def get_fencing_prices(garden, discount):
    visited_plots = set()

    def get_corners(neighbors, plant_type):
        t, r, b, l, tl, tr, br, bl = neighbors
        corners = 0

        def is_corner(tile1, tile2, diagonal_tile):
            # Case 1: Both adjacent tiles are different from current plant type
            if tile1 != plant_type and tile2 != plant_type:
                return True

            # Case 2: Both adjacent tiles are current plant type, but diagonal tile is different
            if tile1 == plant_type and tile2 == plant_type and diagonal_tile != plant_type:
                return True

            return False

        if is_corner(garden[l[0]][l[1]], garden[t[0]][t[1]], garden[tl[0]][tl[1]]):
            corners += 1

        if is_corner(garden[t[0]][t[1]], garden[r[0]][r[1]], garden[tr[0]][tr[1]]):
            corners += 1

        if is_corner(garden[r[0]][r[1]], garden[b[0]][b[1]], garden[br[0]][br[1]]):
            corners += 1

        if is_corner(garden[b[0]][b[1]], garden[l[0]][l[1]], garden[bl[0]][bl[1]]):
            corners += 1

        return corners

    def bfs(i, j, discount):
        if (i, j) in visited_plots:
            return 0

        plant_type = garden[i][j]
        visited_plants = set()
        perimeter = 0
        corners = 0
        q = [(i, j)]

        while q:
            i, j = q.pop(0)
            if (i, j) in visited_plants:
                continue
            visited_plots.add((i, j))
            visited_plants.add((i, j))
            neighbors = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1),
                         (i - 1, j - 1), (i - 1, j + 1), (i + 1, j + 1), (i + 1, j - 1)]
            corners += get_corners(neighbors, plant_type)
            for x, y in neighbors[:4]:
                if garden[x][y] == plant_type:
                    q.append((x, y))
                else:
                    perimeter += 1
        area = len(visited_plants)
        sides = corners

        if discount:
            return area * sides

        return area * perimeter

    return sum(bfs(i, j, discount) for i in range(1, len(garden) - 1) for j in range(1, len(garden[0]) - 1))


# Part One: Get the total price of fencing for the garden plots
print(f'Part One: {get_fencing_prices(garden, discount=False)}')

# Part Two: Get the total price of fencing for the garden plots with a discount
print(f'Part Two: {get_fencing_prices(garden, discount=True)}')
