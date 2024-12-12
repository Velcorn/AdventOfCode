# Read input as list of lists
with open('example.txt') as f:
    garden_plots = [[char for char in line.strip()] for line in f]

