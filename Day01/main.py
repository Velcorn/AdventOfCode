# Split input into two lists of integers, sort lists and calculate the sum of pairwise distances
print(sum(abs(x - y) for x, y in zip(*map(sorted, zip(*[map(int, line.split()) for line in open('input.txt')])))))
