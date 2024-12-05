# Read input file and split it into lines
with open('input.txt') as f:
    lines = f.read().splitlines()

# Part One: Iterate over all 4x4 squares, counting the number of XMAS or SAMX
xmas = ('XMAS', 'SAMX')
xmas_count = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if j <= len(lines[i]) - 4:
            horizontal = lines[i][j:j + 4]
            if horizontal in xmas:
                xmas_count += 1

        if i <= len(lines) - 4:
            vertical = ''.join(lines[i + k][j] for k in range(4))
            if vertical in xmas:
                xmas_count += 1

        if i <= len(lines) - 4 and j <= len(lines[i]) - 4:
            diagonal_lr = ''.join(lines[i + k][j + k] for k in range(4))
            if diagonal_lr in xmas:
                xmas_count += 1

        if i >= 3 and j <= len(lines[i]) - 4:
            diagonal_rl = ''.join(lines[i - k][j + k] for k in range(4))
            if diagonal_rl in xmas:
                xmas_count += 1

print(f"Part One: {xmas_count}")

# Part Two: Iterate over all 3x3 Xs, counting the number of Xs that consist of only MAS and SAM
x_mas = ('MAS', 'SAM')
x_mas_count = 0
for i in range(len(lines) - 2):
    for j in range(len(lines[0]) - 2):
        x = (lines[i][j] + lines[i + 1][j + 1] + lines[i + 2][j + 2] +
             lines[i + 2][j] + lines[i + 1][j + 1] + lines[i][j + 2])
        if x[:3] in x_mas and x[3:] in x_mas:
            x_mas_count += 1

print(f"Part Two: {x_mas_count}")
