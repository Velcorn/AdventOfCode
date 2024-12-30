# Read input as two lists of locks and keys
with open('25_input.txt') as f:
    lines = f.read().splitlines()
    locks = []
    keys = []
    for i in range(0, len(lines), 8):
        line = lines[i]
        if line == '#####':
            lock = [0, 0, 0, 0, 0]
            for j in range(i + 1, i + 7):
                line = lines[j]
                for k, c in enumerate(line):
                    if c == '#':
                        lock[k] += 1
            locks.append(lock)
        else:
            key = [0, 0, 0, 0, 0]
            for j in range(i, i + 6):
                line = lines[j]
                for k, c in enumerate(line):
                    if c == '#':
                        key[k] += 1
            keys.append(key)

# Part One: The number of unique lock/key pairs that fit together
unique_pairs = 0
for lock in locks:
    for key in keys:
        lockey = [l + k for l, k in zip(lock, key)]
        if all(l <= 5 for l in lockey):
            unique_pairs += 1
print(f'Part One: {unique_pairs}')
