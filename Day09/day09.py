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
        free_space.append(d)

# Part One: Compact filesystem and calculate its checksum
compacted = []
while files:
    # Add elements from first file
    block = files.pop(0)
    compacted.extend(block)

    # Fill free space by removing elements from the back of files
    free = free_space.pop(0)
    while free:
        # If no more files, break
        if len(files) == 0:
            break

        # If the last file has fewer elements than free space, add all elements
        block = files[-1]
        if len(block) <= free:
            compacted.extend(block)
            files.pop()
            free -= len(block)
        # Else, add only free elements
        else:
            compacted.extend(block[:free])
            files[-1] = block[free:]
            free = 0

filesystem_checksum = sum(compacted[i] * i for i in range(len(compacted)))
print(f'Part One: {filesystem_checksum}')
