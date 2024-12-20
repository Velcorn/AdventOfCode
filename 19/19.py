# Read input as two lists of strings
with open('19_example.txt') as f:
    lines = f.read().splitlines()
    towel_patterns = lines[0].split(', ')
    designs = [line for line in lines[2:]]


def is_possible(towel_patterns, design):
    return 0


# Part One: Get the number of designs that are possible
print(f'Part One: ')
