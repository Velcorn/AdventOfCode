# Read input file and split it into lines
with open('input.txt') as f:
    word_search = f.read().splitlines()

# Part One: Iterate over all 4x4 squares, counting the number of XMAS or SAMX
xmas = ('XMAS', 'SAMX')
xmas_count = 0
for i in range(len(word_search)):
    for j in range(len(word_search[i])):
        if j <= len(word_search[i]) - 4:
            horizontal = word_search[i][j:j + 4]
            if horizontal in xmas:
                xmas_count += 1

        if i <= len(word_search) - 4:
            vertical = ''.join(word_search[i + k][j] for k in range(4))
            if vertical in xmas:
                xmas_count += 1

        if i <= len(word_search) - 4 and j <= len(word_search[i]) - 4:
            diagonal_lr = ''.join(word_search[i + k][j + k] for k in range(4))
            if diagonal_lr in xmas:
                xmas_count += 1

        if i >= 3 and j <= len(word_search[i]) - 4:
            diagonal_rl = ''.join(word_search[i - k][j + k] for k in range(4))
            if diagonal_rl in xmas:
                xmas_count += 1

print(f"Part One: {xmas_count}")

# Part Two: Iterate over all 3x3 Xs, counting the number of Xs that consist of only MAS and SAM
x_mas = ('MAS', 'SAM')
x_mas_count = 0
for i in range(len(word_search) - 2):
    for j in range(len(word_search[0]) - 2):
        x = (word_search[i][j] + word_search[i + 1][j + 1] + word_search[i + 2][j + 2] +
             word_search[i + 2][j] + word_search[i + 1][j + 1] + word_search[i][j + 2])
        if x[:3] in x_mas and x[3:] in x_mas:
            x_mas_count += 1

print(f"Part Two: {x_mas_count}")
