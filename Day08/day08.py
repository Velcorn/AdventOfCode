# Read input file and split it into a list of lists
with open('input.txt') as f:
    city = [list(line.strip()) for line in f]

# Bounds of the city
width, height = len(city[0]), len(city)

# Create a dictionary containing unique alphanumeric characters (keys) in the city and their coordinates (values)
city_dict = {}
for row_idx, row in enumerate(city):
    for col_idx, cell in enumerate(row):
        if cell.isalnum():
            if cell not in city_dict:
                city_dict[cell] = [(row_idx, col_idx)]
            else:
                city_dict[cell] = city_dict[cell] + [(row_idx, col_idx)]

# Part One: Number of unique locations for antinodes in the city
unique_locations = set()
for coordinates in city_dict.values():
    # Process each pair of coordinates once
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1, n):
            c1, c2 = coordinates[i], coordinates[j]
            diff = (c1[0] - c2[0], c1[1] - c2[1])
            new_c1 = (c1[0] + diff[0], c1[1] + diff[1])
            new_c2 = (c2[0] - diff[0], c2[1] - diff[1])

            # Check bounds and add valid locations to the set
            if 0 <= new_c1[0] < height and 0 <= new_c1[1] < width:
                unique_locations.add(new_c1)
            if 0 <= new_c2[0] < height and 0 <= new_c2[1] < width:
                unique_locations.add(new_c2)

print(f"Part One: {len(unique_locations)}")

