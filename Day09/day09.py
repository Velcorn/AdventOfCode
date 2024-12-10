# Read the input file as a single string
with open('input.txt') as f:
    disk_map = [int(char) for char in f.read().strip()]

# Create separate lists for files and free space
files = []
free_space = []
for i, d in enumerate(disk_map):
    if i % 2 == 0:
        val = i // 2
        files.append([val] * d)
    else:
        if d > 0:
            files.append(['.'] * d)


def compact_files(files, part_two=False):
    compacted = []
    while files:
        file = files.pop(0)

        # If the block is not free space, add it to the compacted list
        if '.' not in file:
            compacted.extend(file)
        # Else fill free space by moving elements from the back of files
        else:
            i = 1
            free = len(file)
            while free:
                try:
                    file = files[-i]
                except IndexError:
                    break
                if '.' in file:
                    i += 1
                    continue
                if len(file) <= free:
                    compacted.extend(file)
                    files.pop(-i)
                    free -= len(file)
                else:
                    if not part_two:
                        # Part One, add only the blocks that fit the free space
                        compacted.extend(file[:free])
                        files[-i] = file[free:]
                        free = 0
                    else:
                        # Part two, try finding a file that fits the free space
                        found = False
                        for i in range(2, len(files) + 1):
                            file = files[-i]
                            if '.' in file:
                                continue
                            if len(file) <= free:
                                compacted.extend(file)
                                files[-i] = ['.' for _ in file]
                                free -= len(file)
                                found = True
                                break
                        # If no suitable file was found, fill free space with dots
                        if not found:
                            compacted.extend(['.'] * free)
                            free = 0

    # Replace all dots with zeros
    return [0 if x == '.' else x for x in compacted]


# Part One: Compact filesystem and calculate its checksum
compacted = compact_files(files.copy())
filesystem_checksum = sum(compacted[i] * i for i in range(len(compacted)))
print(f'Part One: {filesystem_checksum}')

# Part Two: Compact filesystem by moving entire files only and calculate its checksum
compacted = compact_files(files.copy(), part_two=True)
filesystem_checksum = sum(compacted[i] * i for i in range(len(compacted)))
print(f'Part Two: {filesystem_checksum}')
