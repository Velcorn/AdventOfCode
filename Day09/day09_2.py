# Read the input file as a single string
with open('input.txt') as f:
    disk_map = [int(char) for char in f.read().strip()]

# Create separate lists for blocks and files
blocks = []
files = []
for i, d in enumerate(disk_map):
    if i % 2 == 0:
        val = i // 2
        for _ in range(d):
            blocks.append(val)
        files.append([val] * d)
    else:
        if d > 0:
            for _ in range(d):
                blocks.append('.')
            files.append(['.'] * d)


def compact_blocks(blocks):
    i, j = 1, len(blocks) - 1
    while i < j:
        while blocks[i] != '.':
            i += 1
        while blocks[j] == '.':
            j -= 1
        if i < j:
            blocks[i], blocks[j] = blocks[j], blocks[i]
            i += 1
            j -= 1
    # Transform dots to zeros
    return [0 if block == '.' else block for block in blocks]


def compact_files(files):
    moved = set()
    i, j = 0, len(files) - 1
    while i < j:
        while '.' not in files[i]:
            i += 1
        while '.' in files[j]:
            j -= 1
        if i < j:
            # If file already moved, go to the next file
            if files[j][0] in moved:
                j -= 1
                continue
            # If free space is too small, move to the next free space; if exhausted, go to the next file
            elif len(files[i]) < len(files[j]):
                i += 1
                if i == j:
                    i = 0
                    j -= 1
                continue
            # If file fits exactly in the free space, swap them
            elif len(files[i]) == len(files[j]):
                moved.add(files[j][0])
                files[i], files[j] = files[j], files[i]
                i = 0
            # If file does not fit exactly, files[i] becomes files[j], files[j] becomes free space of the same size
            # and files[i] + 1 becomes free space of the remaining size
            else:
                moved.add(files[j][0])
                len_i, len_j = len(files[i]), len(files[j])
                files[i] = files[j]
                files[j] = ['.' for _ in range(len(files[j]))]
                files.insert(i + 1, ['.' for _ in range(len_i - len_j)])
                i = 0

    # Transform dots to zeros
    return [0 if block == '.' else block for file in files for block in file]


# Part One: Compact filesystem and calculate its checksum
compacted = compact_blocks(blocks.copy())
filesystem_checksum = sum(compacted[i] * i for i in range(len(compacted)))
print(f'Part One: {filesystem_checksum}')

# Part Two: Compact filesystem by moving entire files only and calculate its checksum
compacted = compact_files(files.copy())
filesystem_checksum = sum(compacted[i] * i for i in range(len(compacted)))
print(f'Part Two: {filesystem_checksum}')
