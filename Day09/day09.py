# Read the input file as a single string
with open('example.txt') as f:
    disk_map = [int(char) for char in f.read().strip()]

# Create separate lists for files and free space
files = []
free_space = []
for i, d in enumerate(disk_map):
    if i % 2 == 0:
        val = i // 2
        files.append([val] * d)
    else:
        free_space.append(d)


def compact_files(files, free_space, part_two=False):
    compacted = []
    while files:
        # Add elements from the first file
        block = files.pop(0)
        compacted.extend(block)

        # Fill free space by removing elements from the back of files
        free = free_space.pop(0)
        while free:
            # If no more files, break
            if len(files) == 0:
                break

            # If the xth file has fewer elements than free space, add all elements
            block = files[-1]
            if len(block) <= free:
                compacted.extend(block)
                files.pop()
                free -= len(block)
            else:
                if not part_two:
                    # If part one, add only free elements from the last file
                    compacted.extend(block[:free])
                    files[-1] = block[free:]
                    free = 0
                else:
                    # Try finding a file with leq elements than free space
                    found = False
                    for i in range(2, len(files) + 1):
                        block = files[-i]
                        if len(block) <= free:
                            compacted.extend(block)
                            files.pop(-i)
                            free -= len(block)
                            found = True
                            print(compacted)
                            break
                    # If no suitable block was found, fill free space with zeros
                    if not found:
                        compacted.extend([0] * free)
                        free = 0
    return compacted


# Part One: Compact filesystem and calculate its checksum
compacted = compact_files(files.copy(), free_space.copy())
filesystem_checksum = sum(compacted[i] * i for i in range(len(compacted)))
print(f'Part One: {filesystem_checksum}')

# Part Two: Compact filesystem by moving entire files only and calculate its checksum
compacted = compact_files(files.copy(), free_space.copy(), part_two=True)
print(compacted)
filesystem_checksum = sum(compacted[i] * i for i in range(len(compacted)))
print(f'Part Two: {filesystem_checksum}')
