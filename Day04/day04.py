# Read input file
with open('input.txt') as f:
    text = f.read()

# Part One: Extract all horizontal, vertical and diagonal (from left to right and right to left) lines from the input,
# then count the occurrences of the word "XMAS" or "SAMX" (backwards) in all lines
lines = text.splitlines()
horizontal = lines
vertical = [''.join([line[i] for line in lines]) for i in range(len(lines[0]))]
diagonal_lr = [''.join([line[i + j] for j, line in enumerate(lines) if 0 <= i + j < len(line)])
               for i in range(-len(lines), len(lines[0]))]
diagonal_rl = [''.join([line[i - j] for j, line in enumerate(lines) if 0 <= i - j < len(line)])
               for i in range(len(lines[0]) + len(lines) - 1)]
xmas_count = sum(line.count('XMAS') + line.count('SAMX') for line in horizontal + vertical + diagonal_lr + diagonal_rl)
print(f"Part One: {xmas_count}")

# Part Two: Iterate over all 3x3 Xs, counting the number of Xs that consist of only "MAS" or "SAM"
x_mas_count = 0
for i in range(len(lines) - 2):
    for j in range(len(lines[0]) - 2):
        x = (lines[i][j] + lines[i + 1][j + 1] + lines[i + 2][j + 2] +
             lines[i + 2][j] + lines[i + 1][j + 1] + lines[i][j + 2])
        if x.count('MAS') + x.count('SAM') == 2:
            x_mas_count += 1
print(f"Part Two: {x_mas_count}")
