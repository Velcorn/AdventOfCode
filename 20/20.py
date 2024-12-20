# Read the input as list of lists
with open('20_example.txt') as f:
    track = [list(line.strip()) for line in f]


# Part One: The number of cheats that save at least 100 picoseconds
