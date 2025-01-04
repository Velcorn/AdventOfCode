# Read input as string
with open("01_input.txt", 'r') as file:
    directions = file.read()

# Count the number of open and close parentheses
floor = 0
basement = 0
for i, direction in enumerate(directions):
    if direction == '(':
        floor += 1
    else:
        floor -= 1
        # Track the first time direction leads to basement
        if floor == -1 and basement == 0:
            basement = i + 1

# Part One: The floor Santa ends up on
print("Part One:", floor)

# Part Two: The position of the character that causes Santa to first enter the basement
print("Part Two:", basement)
